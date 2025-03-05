from secdown.link_generator import LinkGenerator

def test_generate_quarter_links():
    generator = LinkGenerator()
    links = generator.generate_quarter_links(2021)
    expected = [
        ("https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021q1_notes.zip", "q1"),
        ("https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021q2_notes.zip", "q2"),
        ("https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021q3_notes.zip", "q3"),
        ("https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021q4_notes.zip", "q4"),
    ]
    assert links == expected

def test_generate_month_links():
    generator = LinkGenerator()
    links = generator.generate_month_links(2021)
    expected = [
        (f"https://www.sec.gov/files/dera/data/financial-statement-notes-data-sets/2021_{str(m).zfill(2)}_notes.zip", f"{str(m).zfill(2)}")
        for m in range(1, 13)
    ]
    assert links == expected
