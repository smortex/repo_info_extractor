import re


def extract_libraries(files):
    """Extracts a list of imports that were used in the files

    Parameters
    ----------
    files : []string
        Full paths to files that need to be analysed

    Returns
    -------
    dict
        imports that were used in the provided files, mapped against the language
    """
    # Kotlin import generally look like:
    # import org.example.Message // Message is accessible
    # import org.test.Message as testMessage // testMessage stands for 'org.test.Message'
    # importing Kotlin libraries is very similar to the import structure of java,
    # however there is no import static syntax

    res = []

    # regex to find imports like org.example (exclude standard java kotlin libraries)
    regex_import = re.compile(r'import ((?!kotlin|java)[a-zA-Z0-9]*\.[a-zA-Z0-9]*)', re.IGNORECASE)
    # regex to find imports like org.example.Message
    regex_import_long = re.compile(r'import ((?!kotlin|java)[a-zA-Z0-9]*\.[a-zA-Z0-9]*\.[a-zA-Z0-9]*)', re.IGNORECASE)

    for f in files:
        with open(file=f, mode='r', errors='ignore') as fr:

            contents = ' '.join(fr.readlines())
            matches = regex_import.findall(contents)
            matches.extend(regex_import_long.findall(contents))

        if matches:
            # remove occasional trailing dots
            res.extend([m.rstrip(".") for m in matches])

    # remove duplicates
    res = list(set(res))

    return {"Kotlin": res}
