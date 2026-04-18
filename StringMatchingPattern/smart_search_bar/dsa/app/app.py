"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from enum import Enum

import reflex as rx

from app.dsa.naive import naive
from app.dsa.kmp import kmp
from app.dsa.boyer_moore import bm
from app.data import generate_words

class Algorithm(str, Enum):
    NAIVE = "Naive"
    KMP = "KMP"
    BM = "BM"

SEARCH_LIMIT = 10  # limit results for performance
class State(rx.State):
    """The app state."""
    query: str = ""
    algorithm: Algorithm = Algorithm.NAIVE  # default
    results: list[list[tuple[str, bool]]] = []  # (word, matches, pattern, highlighted_parts)
    operations: int = 0

    data: list[str] = generate_words(10000)  # generate 10k random words of length 5-10

    # Called whenever user types
    @rx.event
    def set_query(self, value: str):
        self.query = value
        self.run_search()

    # Called when algorithm changes
    @rx.event
    def set_algorithm(self, value: str):
        self.algorithm = Algorithm(value)
        self.run_search()

    @rx.var
    def get_algorithms_as_lst(self) -> list[str]:
        return [a.value for a in Algorithm]
    
    def run_search(self):
        self.results = []  # reset results
        self.operations = 0
        if self.query == "":
            return  # skip search if query is empty
        for word in self.data:
            if self.algorithm == Algorithm.NAIVE:
                matches, ops = naive(word, self.query)
                self.operations += ops
            elif self.algorithm == Algorithm.KMP:
                matches, ops = kmp(word, self.query)
                self.operations += ops
            else:
                matches, ops = bm(word, self.query)
                self.operations += ops
            if matches:
                highlighted_parts = get_highlighted_parts(word, self.query, matches)
                self.results.append(highlighted_parts)
            
            if len(self.results) >= SEARCH_LIMIT:
                break

def get_highlighted_parts(word: str, pattern: str, matches: list[int]) -> list[tuple[str, bool]]:
    """Helper function to split word into highlighted and non-highlighted parts."""
    highlighted_parts: list[tuple[str, bool]] = []
    last_end = 0
    
    for index in matches:
        start = index
        end = index + len(pattern)
        # Add the non-highlighted portion before this match
        if start > last_end:
            highlighted_parts.append((word[last_end:start], False))
        # Add the highlighted match
        highlighted_parts.append((word[start:end], True))
        last_end = end
    
    # Add any remaining non-highlighted text
    if last_end < len(word):
        highlighted_parts.append((word[last_end:], False))
    
    return highlighted_parts

def highlight_text(item_highlight_parts: list[tuple[str, bool]]) -> rx.Component:
    return rx.text(
        rx.foreach(
            item_highlight_parts,
            lambda part: rx.el.span(
                part[0],
                style={
                    "backgroundColor": rx.cond(part[1], "yellow", "transparent"),
                    "fontWeight": rx.cond(part[1], "bold", "normal"),
                },
            ),
        )
    )

def search_section():
    return rx.vstack(
        rx.text("Search", font_size="14px", color="gray"),

        rx.input(
            placeholder="Type to search...",
            value=State.query,
            on_change=State.set_query,
            width="100%",
        ),

        rx.hstack(
            rx.text("Algorithm:", font_weight="bold"),

            rx.radio(
                State.get_algorithms_as_lst,
                value=State.algorithm,
                on_change=State.set_algorithm,
            ),
        ),

        spacing="3",
        width="100%",
    )

def results_section():
    return rx.vstack(
        rx.heading("Results", size="4"),

        rx.cond(
            State.query == "",
            rx.text("Start typing to see results...", color="gray"),

            rx.cond(
                State.results.length() == 0,
                rx.text("No matches found.", color="gray"),

                rx.vstack(
                    rx.text(
                        f"{State.results.length()} results found",
                        color="gray",
                        font_size="14px",
                    ),

                    rx.foreach(
                        State.results,
                        lambda item: rx.box(
                            highlight_text(item),
                            padding="10px",
                            border="1px solid #eee",
                            border_radius="8px",
                            width="100%",
                        ),
                    ),

                    spacing="2",
                    width="100%",
                ),
            ),
        ),

        width="100%",
    )

def performance_panel():
    return rx.box(
            rx.text("# of operations", color="gray"),
            rx.heading(f"{State.operations}", size="5"),
            padding="12px",
            border="1px solid #eee",
            border_radius="10px",
            width="100%",
        )

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            # Header
            rx.heading("🔍 Smart Search Demo", size="7"),
            rx.text("Naive vs KMP String Matching"),

            # Search
            search_section(),

            # # Performance
            performance_panel(),

            # Results
            results_section(),

            spacing="6",
            width="600px",
        ),
        center_content=True,
    )


app = rx.App()
app.add_page(index)
