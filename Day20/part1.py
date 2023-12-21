from enum import Enum
import math
from typing import NamedTuple
from abc import ABC, abstractmethod, abstractproperty

modules = {}

class PulseState(Enum):
    high = True
    low = False

    def __eq__(self, other):
        if isinstance(other, bool):
            return self.value == other
        return super().__eq__(other)
    
    def __hash__(self):
        # Since the identity of enum members is unique and immutable, this is safe
        return hash(self.value)

class XmasModule(ABC):
    name: str
    outputs: list[str]

    def __init__(self, detail_string) -> None:
        self.name, outputs = detail_string.split(" -> ")
        if self.name[0] != "b":
            self.name=self.name[1:]
        self.outputs = outputs.split(", ")
        modules[self.name] = self
    
    def generate_pulse_actions(self, pulse: PulseState):
        pulse_actions: list[PulseAction] = []
        for output in self.outputs:
            pulse_actions.append(PulseAction(pulse, modules.get(output), self.name))
        return pulse_actions
    
    @abstractproperty
    def in_default_state(self)->bool:
        pass

    @abstractmethod
    def process_pulse(self, pulse: PulseState, sent_from: str) -> list["PulseAction"]:
        pass

class PulseAction(NamedTuple):
    pulse: PulseState
    module: XmasModule
    from_module_name: str

class FlipFlop(XmasModule):
    state: bool = False

    @property
    def in_default_state(self)->bool:
        return self.state == False

    def process_pulse(self, pulse: PulseState, sent_from: str) -> list[PulseAction]:
        next_pulses: list[PulseAction] = []
        if pulse == PulseState.low:
            self.state = not self.state
            next_pulses = self.generate_pulse_actions(self.state)
        return next_pulses
    
class Conjunction(XmasModule):    
    _last_pulses: dict[str, PulseState] = None

    def initialize_last_pulses(self):
        self._last_pulses = {
            xmas_module.name: PulseState.low 
            for xmas_module in modules.values()
            if self.name in xmas_module.outputs
        }
    
    @property
    def last_pulses(self) -> dict[str, PulseState]:
        if self._last_pulses is None:
            self.initialize_last_pulses()
        return self._last_pulses
    
    @property
    def in_default_state(self)->bool:
        return PulseState.high not in self.last_pulses.values()

    def process_pulse(self, pulse: PulseState, sent_from: str) -> list[PulseAction]:
        self.last_pulses[sent_from] = pulse

        return self.generate_pulse_actions(
            pulse == PulseState.low or PulseState.low in self.last_pulses.values()
        )
    
class Broadcaster(XmasModule):
    @property
    def in_default_state(self)->bool:
        return True
    
    def process_pulse(self, pulse: PulseState, sent_from: str) -> list[PulseAction]:
        return self.generate_pulse_actions(pulse)

prefix_to_type: dict[str, type[XmasModule]] = {
    "%": FlipFlop,
    "&": Conjunction,
    "b": Broadcaster
}

def create_modules():
    with open("input.txt", 'r') as file:
        for line in [line.strip() for line in file]:
            xmas_modules = prefix_to_type[line[0]](line)

def get_pulse_product(button_presses: int) -> int:
    cycle_pulse_hits: list[dict[PulseState, int]] = []
    pulse_hits: dict[PulseState, int] = {
        PulseState.high: 0,
        PulseState.low: 0
    }
    for _ in range(button_presses):        
        pulse_action_stack = [PulseAction(PulseState.low, modules["broadcaster"], "")]
        while pulse_action_stack:
            pulse_action = pulse_action_stack.pop()
            pulse_hits[pulse_action.pulse] += 1
            if pulse_action.module:
                pulse_action_stack += pulse_action.module.process_pulse(pulse_action.pulse, pulse_action.from_module_name)
            
        cycle_pulse_hits.append(pulse_hits.copy())
        if all(module.in_default_state for module in modules.values()):
            break
    
    full_repeats_hit = math.floor(button_presses/len(cycle_pulse_hits))

    total_high = cycle_pulse_hits[-1][PulseState.high] * full_repeats_hit
    total_low = cycle_pulse_hits[-1][PulseState.low] * full_repeats_hit
    
    remaining_cycles = button_presses%len(cycle_pulse_hits)
    if remaining_cycles > 0:
        total_high += cycle_pulse_hits[remaining_cycles-1][PulseState.high]
        total_low += cycle_pulse_hits[remaining_cycles-1][PulseState.low]
    
    return total_high * total_low



create_modules()
print(get_pulse_product(1000))
        

    