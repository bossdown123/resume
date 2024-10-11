from pylatex import Document, Section as LatexSection, Command, NoEscape, Package, Itemize
from datetime import date
from pylatex.utils import bold

class Section:
    def __init__(self, title: str, sub_title: str, start_date: date, end_date: date, loc1: str, loc2: str, points: list[str]):
        self.title = title
        self.sub_title = sub_title
        self.start_date = start_date
        self.end_date = end_date
        if type(end_date) == date:
            if end_date < start_date:
                raise ValueError("End date cannot be before start date")
            if end_date > date.today():
                self.end_date_str = f"{end_date.strftime('%B').title()} {end_date.year} (Expected)"
            else:
                self.end_date_str = f"{end_date.strftime('%B')} {end_date.year}"
        elif type(end_date) == str:
            self.end_date_str = end_date
        else:
            self.end_date_str = ''
        self.loc1 = loc1
        self.loc2 = loc2
        self.points = points

    def __str__(self) -> str:
        return f"{self.title} {self.sub_title} {self.start_date} {self.end_date} {self.loc1} {self.loc2}\n{'\n'.join(self.points)}"


class Section_header:
    def __init__(self, title: str):
        self.title = title
    def __str__(self) -> str:
        return f"{self.title}"


class Header:
    def __init__(self, name: str, email: str, phone: str, github: str, linkedin: str, website: str, address: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.github = github
        self.linkedin = linkedin
        self.website = website
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} {self.email} {self.phone} {self.github} {self.linkedin} {self.website} {self.address}"


class Resume:
    def __init__(self, structure: dict,
                 margin_top=".25in", margin_bottom=".5in", margin_left=".3in", margin_right=".3in",
                 font_size='8pt',
                 spacing_before_section_header='-0.2cm', spacing_after_section_header='-0.5cm',
                 spacing_before_bar='-0.0cm', spacing_after_bar='-0.16cm',
                 spacing_before_each_section='-0.4cm', spacing_after_each_section='0cm',
                 itemize_itemsep='-10pt', itemize_parskip='-4pt'):
        self.structure = structure
        self.margin_top = margin_top
        self.margin_bottom = margin_bottom
        self.margin_left = margin_left
        self.margin_right = margin_right
        self.font_size = font_size
        self.spacing_before_section_header = spacing_before_section_header
        self.spacing_after_section_header = spacing_after_section_header
        self.spacing_before_bar = spacing_before_bar
        self.spacing_after_bar = spacing_after_bar
        self.spacing_before_each_section = spacing_before_each_section
        self.spacing_after_each_section = spacing_after_each_section
        self.itemize_itemsep = itemize_itemsep
        self.itemize_parskip = itemize_parskip

        self.doc = Document(documentclass='article', document_options=[self.font_size, 'letter'])
        self.doc.packages.append(Package('geometry', options=f'top={self.margin_top}, bottom={self.margin_bottom}, left={self.margin_left}, right={self.margin_right}'))
        self.doc.packages.append(Package('hyperref', options='colorlinks=true, linkcolor=blue, urlcolor=blue'))
        self.doc.packages.append(Package('hyphenat', options='none'))
        self.doc.preamble.append(NoEscape(r'\setlength{\parindent}{0pt}'))
        self.doc.preamble.append(NoEscape(r'\sloppy'))
        self.doc.packages.append(Package('enumitem'))
        self.doc.preamble.append(NoEscape(r'\setlist[itemize]{itemsep=-3.25pt, topsep=-3.25pt}'))

    def add_header(self, header: Header):
        self.doc.preamble.append(NoEscape(f'\\title{{\\vspace{{-1.125cm}}\\textbf{{\\Huge {header.name}}}\\vspace{{-0.5cm}}}}'))
        self.doc.preamble.append(Command('author', ''))
        self.doc.preamble.append(Command('date', NoEscape(r'\vspace{-3\baselineskip}')))
        self.doc.append(NoEscape(r'\maketitle'))

        contact_info = []
        if header.email:
            contact_info.append(NoEscape(f"Email: \\href{{mailto:{header.email}}}{{{header.email}}}"))
        if header.phone:
            contact_info.append(NoEscape(f"Phone: {header.phone}"))
        if header.github:
            contact_info.append(NoEscape(f"GitHub: \\href{{{header.github}}}{{{header.github}}}"))
        if header.linkedin:
            contact_info.append(NoEscape(f"LinkedIn: \\href{{{header.linkedin}}}{{{header.linkedin}}}"))
        if header.website:
            contact_info.append(NoEscape(f"Website: \\href{{{header.website}}}{{{header.website}}}"))
        if header.address:
            contact_info.append(f"{header.address}")

        self.doc.append(NoEscape(r'\vspace{' + self.spacing_before_section_header + r'}'))
        self.doc.append(NoEscape(r'\begin{center}' + ' \\ '.join(contact_info) + r'\end{center}'))
        self.doc.append(NoEscape(r'\vspace{' + self.spacing_after_section_header + r'}'))

    def add_sections(self):
        for section in self.structure["sections"]:
            section_header = section["section_header"]
            sections = section["sections"]

            self.doc.append(NoEscape(r'\vspace{' + self.spacing_before_section_header + r'}'))
            self.doc.append(NoEscape(r'\section*{\large\textbf{' + section_header.title + r'}}'))
            self.doc.append(NoEscape(r'\vspace{' + self.spacing_after_section_header + r'}'))

            self.doc.append(NoEscape(r'\noindent\makebox[\linewidth]{\rule{\linewidth}{0.4pt}}'))
            self.doc.append(NoEscape(r'\vspace{' + self.spacing_after_bar + r'}'))  

            for sec in sections:
                self.doc.append(NoEscape(r'\vspace{' + self.spacing_before_each_section + r'}'))  

                title = sec.title if sec.title else ""
                sub_title = sec.sub_title if sec.sub_title else ""
                location = f"{sec.loc1}, {sec.loc2}" if sec.loc1 and sec.loc2 else ""
                if sec.start_date and sec.end_date_str:
                    date_range = f"{sec.start_date.strftime('%B %Y')} - {sec.end_date_str}"
                elif sec.start_date:
                    date_range = f"{sec.start_date.strftime('%B %Y')}"
                else:
                    date_range = ""

                title_with_location = NoEscape(
                    r'\fontsize{10}{12}\selectfont' + r'\textbf{' + title + r'}\hfill' + r'\textit{' + location + r'}'
                )

                with self.doc.create(LatexSection(title_with_location, numbering=False)) as section:
                    if sub_title:
                        subtitle_with_dates = NoEscape(
                            r'\vspace{-0.3cm}\textit{' + sub_title + r'}\hfill' + r'\textit{' + date_range + r'}\vspace{-0.1cm}'
                        )
                        section.append(subtitle_with_dates)

                    with self.doc.create(Itemize()) as itemize:
                        for point in sec.points:
                            itemize.add_item(point)

                self.doc.append(NoEscape(r'\vspace{' + self.spacing_after_each_section + r'}'))  

    def build_resume(self):
        self.doc.append(NoEscape(r'\pagenumbering{gobble}'))

        header = self.structure["header"]
        self.add_header(header)

        self.add_sections()

        self.doc.generate_pdf("sample", clean_tex=False)