import json

from .parser import ParsedData


def print_used_names(data: ParsedData, output_format: str = "text") -> None:
    if output_format == "json":
        print(json.dumps(data.used, indent=2))
    else:
        print("\nUsed (Checked) Project Names by Section:")
        print("=====================================")
        for section, items in data.used.items():
            if items:
                print(f"\n{section}:")
                for item in items:
                    print(f"  - {item}")


def print_unused_names(data: ParsedData, output_format: str = "text") -> None:
    if output_format == "json":
        print(json.dumps(data.unused, indent=2))
    else:
        print("\nUnused (Unchecked) Project Names by Section:")
        print("=======================================")
        for section, items in data.unused.items():
            if items:
                print(f"\n{section}:")
                for item in items:
                    print(f"  - {item}")


def print_all_names(data: ParsedData, output_format: str = "text") -> None:
    if output_format == "json":
        print(json.dumps({"used": data.used, "unused": data.unused}, indent=2))
    else:
        print("\nAll Project Names by Section:")
        print("=========================")
        for section in data.used.keys():
            print(f"\n{section}:")
            if data.used[section]:
                print("\n  Used:")
                for item in data.used[section]:
                    print(f"    - {item}")
            if data.unused[section]:
                print("\n  Unused:")
                for item in data.unused[section]:
                    print(f"    - {item}")
