from collections import deque
from enum import Enum
import math
from typing import NamedTuple
from abc import ABC, abstractmethod, abstractproperty
import itertools

modules: dict[str, "XmasModule"] = {}

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
    
class Ender(XmasModule):
    outputs = []
    
    def __init__(self, name:str) -> None:
        self.name = name

    @property
    def in_default_state(self)->bool:
        pass

    def process_pulse(self, pulse: PulseState, sent_from: str) -> list[PulseAction]:            
        return []



prefix_to_type: dict[str, type[XmasModule]] = {
    "%": FlipFlop,
    "&": Conjunction,
    "b": Broadcaster
}

def create_modules(ender:str):
    with open("input.txt", 'r') as file:
        for line in [line.strip() for line in file]:
            xmas_modules = prefix_to_type[line[0]](line)

    modules[ender] = Ender(ender)

def get_ending_button_press(ender:str) -> int:
    direct_children = {}
    for button_press in itertools.count():
        modules[ender].in_end_state = False
        modules[ender].hit_count = 0
        pulse_action_stack = [PulseAction(PulseState.low, modules["broadcaster"], "")]
        while pulse_action_stack:
            pulse_action = pulse_action_stack.pop()
            if pulse_action.module:
                if pulse_action.module.name == "lv" and pulse_action.pulse == True:
                    if direct_children.get(pulse_action.from_module_name) is None:
                        direct_children[pulse_action.from_module_name] = button_press + 1
                    if len(direct_children.keys()) == len(pulse_action.module.last_pulses.keys()):
                        return math.lcm(*direct_children.values())
                pulse_action_stack += pulse_action.module.process_pulse(pulse_action.pulse, pulse_action.from_module_name)



create_modules("rx")
print(get_ending_button_press("rx"))
        

    