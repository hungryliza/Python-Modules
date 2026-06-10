from typing import Callable
import functools
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def timed(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        timed1 = time.time()
        res = func(*args, **kwargs)
        timed2 = time.time()
        print(f"Spell completed in {(timed2 - timed1):.3f} seconds")
        return res
    return timed

def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args[0] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    res = func()
                    return res
                except Exception:
                        print(f"Spell failed, retrying... (attempt {i + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for char in name:
                if not char.isalpha() and not char.isspace():
                    return False
            return True
        else:
            return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(min_power=10)
        def pow_spell(power):
            return f"Successfully cast {spell_name} with {power} power!"
        res = pow_spell(power)
        return res

if __name__ == "__main__":
    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Result : Fireball cast!"

    print(fireball())
    print()

    @retry_spell(max_attempts=3)
    def spell_retrier_fail():
        raise Exception("raising exception for testing")

    print()
    print("Testing retrying spell...")
    print(spell_retrier_fail())

    print()
    print("Testing MageGuild...")
    mages = MageGuild()
    print(mages.validate_mage_name("Ricky"))
    print(mages.validate_mage_name("Ri"))
    print(mages.cast_spell("Fireball", 10))
    print(mages.cast_spell("Fireball", 5))
