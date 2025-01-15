def substring_count(main_string, substring):
    """Count occurrences of a substring in a given string."""
    return main_string.count(substring)


if __name__ == '__main__':
    main_string = 'APT APT APT APT APT'
    substring = 'APT'
    result = substring_count(main_string, substring)
    print(result)