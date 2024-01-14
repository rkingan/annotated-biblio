"""

Data model - basically the class representing a paper, plus code to parse/produce bibtex

"""
import bibtexparser
import dateutil.parser

from dataclasses import dataclass
from datetime import date
from typing import List, Optional

@dataclass
class Paper:
    name: str
    title: str
    authors: List[str]
    journal: str
    year: str
    date_seen: date
    volume: Optional[str] = None
    number: Optional[str] = None
    pages: Optional[str] = None
    abstract: Optional[str] = None
    date_read: Optional[date] = None
    notes: Optional[str] = None


class _FieldBuilder:
    def __init__(self):
        self.line_no = 1
        self.fields = []

    def add_field(self, name: str, value: str) -> bibtexparser.model.Field:
        """

        Builds a Field instance and increments the line counter

        """
        if value is not None:
            result = bibtexparser.model.Field(name, value, self.line_no)
            self.fields.append(result)
            self.line_no += 1


def _encode_authors(author_names: List[str]) -> str:
    return " and ".join(author_names)


def _encode_date(d: date) -> str:
    if d is None:
        return None
    return d.isoformat()


def entry_from_paper(paper: Paper) -> bibtexparser.model.Entry:
    """

    Generates a bibtex file entry from an instance of Paper

    Parameters
    ----------

    paper : Paper

        Paper to encode

    Returns
    -------

    bibtexparser.model.Entry

        Entry that can be written into a bibtex file

    """
    builder = _FieldBuilder()
    builder.add_field("author", _encode_authors(paper.authors))
    builder.add_field("title", paper.title)
    builder.add_field("journal", paper.journal)
    builder.add_field("year", paper.year)
    builder.add_field("volume", paper.volume)
    builder.add_field("date_seen", _encode_date(paper.date_seen))
    builder.add_field("number", paper.number)
    builder.add_field("pages", paper.pages)
    builder.add_field("abstract", paper.abstract)
    builder.add_field("date_read", _encode_date(paper.date_read))
    builder.add_field("notes", paper.notes)

    return bibtexparser.model.Entry(
        "article",
        paper.name,
        builder.fields
    )


def _get_required_value(entry: bibtexparser.model.Entry, key: str) -> str:
    if key not in entry.fields_dict:
        raise ValueError(f"Required key {key} not found in bibtex entry {entry.key}")

    return entry.fields_dict[key].value


def _get_optional_value(entry: bibtexparser.model.Entry, key: str) -> str:
    field = entry.fields_dict.get(key)
    if field:
        return field.value
    return None


def _parse_authors(author_bibtex: str) -> List[str]:
    return str.split(" and ")


def _parse_date(s: str) -> date:
    if s is None or s == "":
        return None
    return dateutil.parser.isoparse(s).date()


def paper_from_entry(entry: bibtexparser.model.Entry) -> Paper:
    """

    Converts a bibtex entry to a Paper instance

    Parameters
    ----------

    entry : bibtexparser.model.Entry

        bibtex entry for a paper

    Returns
    -------

    Paper

        paper instance

    """
    name = entry.key
    authors = _parse_authors(_get_required_value(entry, "author"))
    title = _get_required_value(entry, "title")
    journal = _get_required_value(entry, "journal")
    year = _get_required_value(entry, "year")
    date_seen = _parse_date(_get_required_value(entry, "date_seen"))
    volume = _get_optional_value(entry, "volume")
    number = _get_optional_value(entry, "number")
    pages = _get_optional_value(entry, "pages")
    abstract = _get_optional_value(entry, "abstract")
    date_read = _parse_date(_get_optional_value(entry, "date_read"))
    notes = _get_optional_value(entry, "notes")

    return Paper(
        name,
        title,
        authors,
        journal,
        year,
        date_seen,
        volume,
        number,
        pages,
        abstract,
        date_read,
        notes
    )


def library_from_papers(papers: List[Paper]) -> bibtexparser.Library:
    """

    Generates a bibtex library from a list of Paper instances.

    Parameters
    ----------

    papers : List[Paper]

        list of Paper instances

    Returns
    -------

    bibtexparser.Library

        Library that can be written to a bibtex file

    """
    entries = [entry_from_paper(paper) for paper in papers]
    result = bibtexparser.Library(entries)
    return result


def papers_from_library(library: bibtexparser.Library) -> List[Paper]:
    """

    Generates a list of Paper instances from a bibtex library.

    Parameters
    ----------

    library : bibtexparser.Library

        Library parsed from bibtex file

    Returns
    -------

    List[Paper]

        List of Paper instances

    """
    return [paper_from_entry(entry) for entry in library.entries]