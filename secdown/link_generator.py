class LinkGenerator:
    def __init__(self):
        """Initializes the link generator"""

    def generate_quarter_links(self, year: int) -> list:
            """
            Genera enlaces trimestrales para un año dado.

            :param year: Año para el cual se generarán los enlaces.
            :return: Lista de enlaces trimestrales.

            Examples:
            --------
            >>> sec = SECDatasetDownloader()
            >>> sec.__generate_quarter_links(2021)
            [ ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021q1_notes.zip', 'q1'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021q2_notes.zip', 'q2'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021q3_notes.zip', 'q3'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021q4_notes.zip', 'q4')]
            """

            return [(f"https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/{year}q{q}_notes.zip", f"q{q}") for q in range(1, 5)]

    def generate_month_links(self, year: int) -> list:
        """
        Genera enlaces mensuales para un año dado.

        :param year: Año para el cual se generarán los enlaces.
        :return: Lista de enlaces mensuales.

        Examples:
        --------
        >>> sec = SECDatasetDownloader()
        >>> sec.__generate_month_links(2021)
        [ ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_01_notes.zip', '01'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_02_notes.zip', '02'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_03_notes.zip', '03'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_04_notes.zip', '04'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_05_notes.zip', '05'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_06_notes.zip', '06'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_07_notes.zip', '07'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_08_notes.zip', '08'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_09_notes.zip', '09'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_10_notes.zip', '10'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_11_notes.zip', '11'), ('https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_12_notes.zip', '12')]
        """

        return [(f"https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/{year}_{str(m).zfill(2)}_notes.zip", f"{str(m).zfill(2)}") for m in range(1, 13)]
