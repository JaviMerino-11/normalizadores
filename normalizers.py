from typing import List
from normalizer_functions.lower_case import lower_case_normalizer
from normalizer_functions.no_accents_nor_specialcharac import no_accents_nor_specialcharac
from normalizer_functions.remove_double_white_spaces import remove_several_white_spaces


def normalizer(phrase_list: List[str], result: List[str] = None) -> None:
    lower_case_normalizer(phrase_list)
    no_accents_nor_specialcharac(phrase_list)
    remove_several_white_spaces(phrase_list)


def normalizer2(phrase_list: List[str], result: List[str] = None) -> None:
    no_accents_nor_specialcharac(phrase_list)
    remove_several_white_spaces(phrase_list)


def main() -> None:
    phrase_list = ['HOLA', 'múndó', 'ñoño', 'cosas     que haCer']
    phrase_list2 = phrase_list
    print('INPUT (LIST 1): %s' % phrase_list)
    print('INPUT (LIST 2): %s' % phrase_list2)

    normalizer2(phrase_list)
    normalizer(phrase_list2)

    print('OUTPUT (LIST 1 all normalizers): %s' % phrase_list)

    print('OUTPUT (LIST 2 only special and white spaces normalized): %s' % phrase_list2)


if __name__ == '__main__':
    main()
