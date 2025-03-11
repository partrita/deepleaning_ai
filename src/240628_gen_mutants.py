import pandas as pd


def generate_mutant(wt_sequence, mutation):
    """
    주어진 WT 서열에서 뮤턴트 서열을 생성하는 함수
    :param wt_sequence: 원래 단백질 서열 (WT 서열)
    :param mutation: 뮤턴트 정보 (예: S239D)
    :return: 뮤턴트 서열
    """
    wild_type_aa = mutation[0]
    position = int(mutation[1:-1])
    mutant_aa = mutation[-1]

    index = position - 118

    if index < 0 or index >= len(wt_sequence):
        raise ValueError(
            f"Mutation position {position} is out of range for the sequence."
        )

    mutant_sequence = list(wt_sequence)

    if mutant_sequence[index] != wild_type_aa:
        raise ValueError(
            f"Expected {wild_type_aa} at position {position} but found {mutant_sequence[index]}."
        )

    mutant_sequence[index] = mutant_aa
    # print(f"{mutation} changed!")

    return "".join(mutant_sequence)


def generate_mutant_dict(seq_wt, mutant_list):
    """
    주어진 WT 서열과 뮤턴트 리스트로부터 뮤턴트 서열 딕셔너리를 생성하는 함수
    :param seq_wt: 원래 단백질 서열 (WT 서열)
    :param mutant_list: 뮤턴트 리스트
    :return: 뮤턴트 서열 딕셔너리
    """
    mutant_sequences = {}

    for protein, mutations in mutant_list.items():
        mutant_sequences[protein] = []
        for mutation in mutations:
            mutant_seq = generate_mutant(seq_wt, mutation)
            mutant_sequences[protein].append(mutant_seq)

    return mutant_sequences


def dict_to_fasta(seq_dict):
    """
    딕셔너리를 FASTA 형식의 문자열로 변환하는 함수
    :param seq_dict: 서열이 저장된 딕셔너리
    :return: FASTA 형식의 문자열
    """
    fasta_string = ""
    for header, sequences in seq_dict.items():
        for sequence in sequences:
            fasta_string += f">{header}\n{sequence}\n"
    return fasta_string


def sequences_to_dataframe(sequences):
    """
    주어진 서열을 데이터프레임으로 변환하는 함수
    :param sequences: 단백질 서열 리스트
    :return: 변환된 데이터프레임
    """
    df = pd.DataFrame()

    for i, sequence in enumerate(sequences):
        df[f"{i + 1}"] = list(sequence)

    df.index = range(118, 118 + len(df))
    return df


def generate_construct_dict(seq_dict: dict):
    """
    주어진 접두사와 접미사를 사용하여 생성된 construct 딕셔너리를 반환하는 함수
    :return: 생성된 construct 딕셔너리
    """
    # Extract segment names and their corresponding sequence lists
    # names = seq_dict.keys()
    # sequences = seq_dict.values()

    construct_dict = {}
    fab = [
        "aHER2",
        "aHER3",
    ]
    fc = [
        "Abv_DE",
        "Abv_KK",
        "Abv_Knob",
        "Abv_Hole",
        "Zeno_DE",
        "Zeno_KK",
        "Zeno_Knob",
        "Zeno_Hole",
    ]

    for nterm in fab:
        for cterm in fc:
            key = f"{nterm}_{cterm}"
            value = eval(f"{nterm} + {cterm}")
            construct_dict[key] = value

    return construct_dict


if __name__ == "__main__":
    seq_wt = "ASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK".strip()

    mutant_list = {
        "DLE": ["S239D", "A330L", "I332E"],
        "AEFT": ["G236A", "I332E", "H268F", "S324T"],
        "GAALIE": ["G236A", "A330L", "I332E"],
        "GAALIELS": ["G236A", "A330L", "I332E", "M428L", "N434S"],
        "SDIEALGA": ["G236A", "S239D", "A330L", "I332E"],
        "SDIEALGALS": ["G236A", "S239D", "A330L", "I332E", "M428L", "N434S"],
        "VLPLL": ["L235V", "F243L", "R292P", "Y300L", "P396L"],
        "LPLL": ["F243L", "R292P", "Y300L", "P396L"],
        "SDIEGA": ["G236A", "S239D", "I332E"],
        "LET": ["F243L", "D270E", "K392T"],
        "LPL": ["F243L", "R292P", "Y300L"],
        "LLEK": ["F243L", "P247L", "D270E", "N421K"],
        "LPIL": ["F243L", "R292P", "V305I", "P396L"],
        "FALE": ["G237F", "S298A", "A330L", "I332E"],
        "EIYE": ["S239E", "V264I", "A330Y", "I332E"],
        "SDIESA": ["S239D", "S298A", "I332E"],
        "LALA": ["L234A", "L235A"],
        "G236A": ["G236A"],
        "Y300L": ["Y300L"],
        "D270E": ["D270E"],
        "KWES": ["K326W", "E333S"],
        "FT": ["H268F", "S324T"],
        "ID": ["L234I", "L235D"],
        "I332E": ["I332E"],
        "F243L": ["F243L"],
        "E258H": ["E258H"],
        "T223K": ["T223K"],
        "K246H": ["K246H"],
        "L328A": ["L328A"],
        "IQ": ["P247I", "A339Q"],
        "DE": ["S239D", "I332E"],
    }

    mutant_sequences = generate_mutant_dict(seq_wt, mutant_list)
    fasta_mutant_sequences = dict_to_fasta(mutant_sequences)
    print(fasta_mutant_sequences)
