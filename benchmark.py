import timeit

from ifs_tasks_escalated import handle as ifs_nested
from match_8_models_type_adapter import handle as match_pydantic_models_with_any
from match_5 import handle as match_on_dicts
from match_8_models_discriminant_union import handle as match_pydantic_models_with_discriminant_union

data = {"type": "AccountUpdated", "id": "fede79b2", "old_status": "paid", "new_status": "trial"}

SAMPLES = 10_000

ifs = timeit.timeit(lambda: ifs_nested(data), number=SAMPLES)
match_dicts = timeit.timeit(lambda: match_on_dicts(data), number=SAMPLES)
match_pydantic = timeit.timeit(lambda: match_pydantic_models_with_any(data), number=SAMPLES)
match_pydantic_optimized = timeit.timeit(lambda: match_pydantic_models_with_discriminant_union(data), number=SAMPLES)

print(f"ifs_nested: {ifs}")
print(f"match_on_dicts: {match_dicts}")
print(f"match_pydantic_models_with_any: {match_pydantic}")
print(f"match_pydantic_models_with_discriminant_union: {match_pydantic_optimized}")

print(f"ifs are faster than match on dicts {round(match_dicts / ifs, 2)} times")
print(f"match on dicts is faster than match on pydantic models {round(match_pydantic / match_dicts, 2)} times")
print(f"ifs are faster than match on pydantic models {round(match_pydantic / ifs, 2)} times")
print(f"ifs are faster than match on pydantic models with discriminant union {round(match_pydantic_optimized / ifs, 2)} times")

print(
    f"Absolute times are:\n"
    f" ifs: {ifs / SAMPLES}s\n"
    f" match_dicts: {match_dicts / SAMPLES}s\n"
    f" match_pydantic: {match_pydantic / SAMPLES}s\n"
    f" match_pydantic_optimized: {match_pydantic_optimized / SAMPLES}s"
)
