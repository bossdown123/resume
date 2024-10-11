import numpy as np
from datetime import *

import resume_struct
from resume_struct import *

header = Header(
    "John Doe",
    "john.doe@example.com",
    "+1 234 567 8901",
    None,
    "https://www.linkedin.com/in/johndoe/",
    None,
    "New York, USA",
)

section_header1 = Section_header(
    "Education",
)
section1 = Section(
    "Lorem Ipsum University",
    "BSc Placeholder Studies",
    date(2020, 9, 1),
    date(2024, 6, 1),
    "Lorem City",
    "Country",
    [
        "Major: Placeholder Studies | Grade: Lorem",
        "Concentration: Placeholder Concentration",
        "Relevant Coursework: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
    ],
)
section2 = Section(
    "Dolor Sit Amet College",
    "BSc Placeholder Field",
    date(2018, 5, 1),
    date(2019, 5, 1),
    "Dolor City",
    "Country",
    [
        "Major: Placeholder Field | GPA: 4.0",
    ],
)

section_header2 = Section_header(
    "Work Experience",
)
section3 = Section(
    "Lorem Corporation",
    "Software Developer - Placeholder Team - Intern",
    date(2022, 6, 1),
    date(2022, 9, 1),
    "Lorem City",
    "Country",
    [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    ],
)

section4 = Section(
    "Placeholder Inc",
    "Software Developer - Data Team - Full Time Placement",
    date(2023, 6, 1),
    date(2024, 6, 1),
    "Dolor City",
    "Country",
    [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    ],
)

section_header3 = Section_header(
    "Leadership and Extracurricular Activities",
)
section5 = Section(
    "Lorem Ipsum Tech Fair - Innovative Project Design and Development - Team Leader",
    "Placeholder Technologies - Python - Docker - React",
    date(2021, 7, 1),
    date(2022, 4, 1),
    "Lorem City",
    "Country",
    [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sollicitudin orci vitae sapien placerat, ac cursus sapien cursus.",
        "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.",
    ]
)
section_header4 = Section_header(
    "Personal Projects",
)
section6 = Section(
    "Placeholder Project 1",
    "Lorem - Ipsum - Dolor - Sit - Amet",
    None,
    None,
    None,
    None,
    [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    ],
)

section7 = Section(
    "Placeholder Project 2",
    "Lorem - Ipsum - Dolor - Sit - Amet",
    None,
    None,
    None,
    None,
    [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    ],
)

section_header5 = Section_header(
    "Skills and Interests",
)
section8 = Section(
    "Technical Skills",
    None,
    None,
    None,
    None,
    None,
    [
        "Advanced: Lorem, Ipsum, Dolor, Sit, Amet",
        "Intermediate: Consectetur, Adipiscing, Elit, Sed, Do, Eiusmod",
    ],
)

section9 = Section(
    "Personal Interests",
    None,
    None,
    None,
    None,
    None,
    [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    ],
)

resume = Resume({
    "header": header,
    "sections": [
        {
            "section_header": section_header1,
            "sections": [section1, section2],
        },
        {
            "section_header": section_header2,
            "sections": [section3, section4],
        },
        {
            "section_header": section_header3,
            "sections": [section5],
        },
        {
            "section_header": section_header4,
            "sections": [section6, section7],
        },
        {
            "section_header": section_header5,
            "sections": [section8, section9],
        }
    ]
})

resume.build_resume()