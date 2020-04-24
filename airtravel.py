"""Model for aircraft flights."""
from pprint import pprint as pp


class Flight:
    def __init__(self, number, aircraft):
        airline_code = number[:2]
        if not airline_code.isalpha():
            raise ValueError(f'No airline code in {number}')
        if not airline_code.isupper():
            raise ValueError(f'Incorrect airline code in {number}')
        if not number[2:].isdigit() and int(number[2:]) < 9999:
            raise ValueError(f'Incorrect route number: {number}')
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        # empty row +
        # set comprehension iterated by letters
        # in list comprehension iterated by numbers
        # we want to create a distinct dictionary object for each for
        # bad approach: [{letter: None for letter in seats}] * len(rows)
        self._seatings = [None] + \
            [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def route(self):
        return self._number[2:]

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f'Invalid seat letter {letter}')
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row {row_text}')
        if row not in rows:
            raise ValueError(f'Invalid row number: {row}')

        return row, letter

    def allocate_seat(self, seat, passanger):
        row, letter = self._parse_seat(seat)
        if self._seatings[row][letter] != None:
            raise ValueError(f'Seat is already taken')

        self._seatings[row][letter] = passanger

    def relocate_passanger(self, old_seat, new_seat):
        old_row, old_letter = self._parse_seat(old_seat)
        if self._seatings[old_row][old_letter] == None:
            return
        new_row, new_letter = self._parse_seat(new_seat)
        if self._seatings[new_row][new_letter] != None:
            raise ValueError(f"Can't relocate, seat {new_seat} already taken")

        self._seatings[new_row][new_letter] = self._seatings[old_row][old_letter]
        self._seatings[old_row][old_letter] = None

    def _num_available_seats(self):
        return sum(
            sum(1 for item in row.values() if item is None)
            for row in self._seatings
            if row is not None
        )

    def _passanger_seats(self):
        for index, row in enumerate(self._seatings):
            if row is None:
                continue
            for letter in row:
                if row[letter] is not None:
                    yield str(index) + letter, row[letter]

    def make_boarding_cards(self, card_printer):
        for seat, passanger in self._passanger_seats():
            card_printer(passanger, seat, self.number(), self.aircraft_model())


class Aircraft:
    def __init__(self, registration, model, num_rows, num_sets_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_sets_per_row = num_sets_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHIJ"[:self._num_sets_per_row])


def console_card_printer(passanger, seat, flight_number, aircraft):
    output = f"| Name: {passanger}"     \
        f"  Flight: {flight_number}"    \
        f"  Seat: {seat}"               \
        f"  Aircraft: {aircraft}"       \
        " |"
    banner = '+' + '-' * (len(output) - 2) + '+'
    boarder = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, boarder, output, boarder, banner]
    card = "\n".join(lines)
    print(card)
    print()


a = Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_sets_per_row=6)
f = Flight('SN0606', a)
print(f._num_available_seats())
f.allocate_seat('6F', 'John')
f.allocate_seat('5F', 'Mary')
f.allocate_seat('2D', 'Harry')
print(f._num_available_seats())
pp(f._seatings)
console_card_printer("John", "12F", "SN106", "Tupolew")
print(next(f._passanger_seats()))
f.make_boarding_cards(console_card_printer)
