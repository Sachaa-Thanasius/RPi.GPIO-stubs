"""GPIO functionality of a Raspberry Pi using Python."""

from collections.abc import Callable
from typing import Final, Literal
from typing_extensions import TypeAlias

_Callback: TypeAlias = Callable[[int], object]
VERSION: Final[str] = ...

HIGH: Final[Literal[1]] = ...
LOW: Final[Literal[0]] = ...
OUT: Final[Literal[0]] = ...
IN: Final[Literal[1]] = ...
HARD_PWM: Final[Literal[43]] = ...
SERIAL: Final[Literal[40]] = ...
I2C: Final[Literal[42]] = ...
SPI: Final[Literal[41]] = ...
UNKNOWN: Final[Literal[-1]] = ...
BOARD: Final[Literal[10]] = ...
BCM: Final[Literal[11]] = ...
PUD_OFF: Final[Literal[20]] = ...
PUD_UP: Final[Literal[22]] = ...
PUD_DOWN: Final[Literal[21]] = ...
RISING: Final[Literal[31]] = ...
FALLING: Final[Literal[32]] = ...
BOTH: Final[Literal[33]] = ...

def setup(
    channel: int | list[int] | tuple[int, ...],
    direction: Literal[0, 1],
    pull_up_down: int = 20,
    initial: int = -1,
) -> None:
    """Set up a GPIO channel or list of channels with a direction and (optional) pull/up down control.

    Parameters
    ----------
    channel: :class:`int` | list[:class:`int`] | tuple[:class:`int`, ...]
        Either board pin number or BCM number depending on which mode is set.
    direction: Literal[0, 1]
        IN or OUT, 1 or 0 respectively.
    pull_up_down: :class:`int`, default=20
        20, 21, or 22, corresponding to PUD_OFF (default), PUD_UP or PUD_DOWN.
    initial: :class:`int`, default=-1
        Initial value for an output channel.
    """

def cleanup(channel: int | list[int] | tuple[int, ...] | None = None) -> None:
    """Clean up by resetting all GPIO channels that have been used by this program to INPUT with no pullup/pulldown and no event detection.

    Arguments
    ---------
    channel: :class:`int` | list[int] | tuple[int, ...] | None, optional
        Individual channel or list/tuple of channels to clean up. The default cleans every channel that has been used.
    """

def output(
    channel: int | list[int] | tuple[int, ...],
    value: int | bool | list[int | bool] | tuple[int | bool, ...],
    /,
) -> None:
    """Output to a GPIO channel or list of channels.

    Arguments
    ---------
    channel: :class:`int` | list[:class:`int`] | tuple[:class:`int`, ...]
        Either board pin number or BCM number depending on which mode is set.
    value: Literal[0, 1] | :class:`bool` | list[:class:`int` | :class:`bool`] | tuple[:class:`int` | :class:`bool`, ...]
        0/1 or False/True or LOW/HIGH.
    """

def input(channel: int, /) -> int:  # noqa: A001
    """Input from a GPIO channel.

    Parameters
    ----------
    channel: :class:`int`
        Either board pin number or BCM number depending on which mode is set.

    Returns
    -------
    :class:`int`:
        HIGH=1=True or LOW=0=False
    """

def setmode(mode: int, /) -> None:
    """Set up numbering mode to use for channels.

    Parameters
    ----------
    mode: Literal[10, 11]
        Only valid inputs are 10 or GPIO.BOARD (uses Raspberry Pi board numbers) and
        11 or GPIO.BCM (uses Broadcom GPIO 00..nn numbers).
    """

def getmode() -> int | None:
    """Get numbering mode used for channel numbers.

    Returns
    -------
    :class:`int` | None
        Returns 10 (GPIO.BOARD), 11 (GPIO.BCM), or None.
    """

def add_event_detect(gpio: int, edge: int, callback: _Callback | None = None, bouncetime: int = -666) -> None:
    """Enable edge detection events for a particular GPIO channel.

    Parameters
    ----------
    channel: :class:`int`
        Either board pin number or BCM number depending on which mode is set.
    edge: :class:`int`
        GPIO.RISING, GPIO.FALLING or GPIO.BOTH.
    callback: Callable[[int], object], optional
        A callback function for the event (optional).
    bouncetime: :class:`int`, default=-666
        Switch bounce timeout in ms for callback.
    """

def remove_event_detect(channel: int, /) -> None:
    """Remove edge detection for a particular GPIO channel.

    Parameters
    ----------
    channel: :class:`int`
        Either board pin number or BCM number depending on which mode is set.
    """

def event_detected(channel: int, /) -> bool:
    """Returns True if an edge has occurred on a given GPIO. You need to enable edge detection using add_event_detect() first.

    Parameters
    ----------
    channel: :class:`int`
        Either board pin number or BCM number depending on which mode is set.
    """

def add_event_callback(gpio: int, callback: _Callback) -> None:
    """Add a callback for an event already defined using add_event_detect().

    Parameters
    ----------
    channel: :class:`int`
        Either board pin number or BCM number depending on which mode is set.
    callback: Callable[[int], object]
        A callback function.
    """

def wait_for_edge(channel: int, edge: int, bouncetime: int = -666, timeout: int = -1) -> int | None:
    """Wait for an edge. Returns the channel number or None on timeout.

    Parameters
    ----------
    channel: :class:`int`
        Either board pin number or BCM number depending on which mode is set.
    edge: :class:`int`
        31/GPIO.RISING, 32/GPIO.FALLING or 33/GPIO.BOTH.
    bouncetime: :class:`int`, default=-666
        Time allowed between calls to allow for switchbounce. Defaults to -666, which means no time.
    timeout: :class:`int`, default=-1
        Timeout in ms. Defaults to -1, which means no time.
    """

def gpio_function(channel: int, /) -> int:
    """Return the current GPIO function (IN, OUT, PWM, SERIAL, I2C, SPI).

    Parameters
    ----------
    channel: :class:`int`
        Either board pin number or BCM number depending on which mode is set.
    """

def setwarnings(state: int, /) -> None:
    """Enable or disable warning messages.

    state: :class:`int`
        0 to disable, 1 to enable. Enabled by default without calling this function.
    """

class PWM:
    """Pulse Width Modulation class"""
    def __init__(self, channel: int, frequency: float, /) -> None: ...
    def start(self, dutycycle: float) -> None:
        """Start software PWM.

        Parameters
        ----------
        dutycycle: :class:`float`
            The duty cycle (0.0 to 100.0).
        """

    def ChangeDutyCycle(self, dutycycle: float, /) -> None:
        """Change the duty cycle.

        dutycycle: :class:`float`
            The new duty cycle (0.0 to 100.0).
        """

    def ChangeFrequency(self, frequency: float, /) -> None:
        """Change the frequency.

        frequency: :class:`float`
            Frequency in Hz (freq > 1.0).
        """

    def stop(self) -> None:
        """Stop software PWM"""