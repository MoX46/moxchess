# Outline of requirements

## CLI
The CLI will be user accessible and also used by the front end GUI

### Functions
```python
moxchess.Game(fen:str = '') -> Game
```

Returns a new game position using fen string. Returns a starting postion if no fen provided

**Arguments**
*fen (Optional)*: a fen string for a position. If not string is provided, the new game fen string is used
**Return**
A Game object

---

```python
moxchess.import(pgn:str) -> Game
```
Returns a game based on input PGN string

**Arguments**
*pgn*: a PGN string representing a game
**Return**
A Game object

---

```python
Game.make_move(move:str) -> None
```
Used to move piece in the game

**Arguments**
*move*: a string representing the move to be played, ex: Qxe4
**Return**
None

---

```python
Game.move(piece:GamePiece,to_square:Square,promote_to:[Piece]=None,take:GamePiece=None) -> None
```
Used to make a move by specifiying a GamePiece object and a square to move to. Optionally specify a piece to promote to and a peice to take.

**Arguments**
*piece*: A GamePice to move
*to_square*: A Square to move to
*promote_to (Optional)*: A Piece to promote to
*take (Optional)*: A GamePice to take
**Return**
None

---

```python
Game.previous() -> None
```
Used to change game state to previous move

**Arguments**
None
**Return**
None

---

```python
Game.legal_moves(piece:GamePice = None) -> list[str]
```
Used to return a list of valid moves for the entire board, or for a specific piece

**Arguments**
*piece (Optional)*: GamePice for which to return valid moves
**Return**
A list of all valid moves in the position if no piece is specified.

---

```python
Game.pieces(type:Pieces = None, color:Colors = None) -> list[GamePice]
```
Used to return all the pieces in the game, pieces of a certain type, or of a certin color

**Arguments**
*type (Optional)*: Specify Pieces object to return only of that type
*color (Optionl)*: Specify Colors object to return only of that color
**Returns**
A list of GamePiece objects

---

```python
Game.turn() -> Colors
```
Returns which color is to move next

**Arguments**
None
**Returns**
Colors object

---

```python
Game.castling_rights() -> dict[GamePice, CastlingDirection]
```
Returns castling moves available

**Arguments**
None
**Returns**

---

```python
Game.ep() ->
```
Returns en passant avaiabiilty

**Arguments**

**Returns**

---

```python
Game.halfmove() -> int
```
Returns the halfmove clock which represents number of moves since last capture or pawn move

**Arguments**
None
**Returns**
integer

---

```python
Game.fullmove() -> int
```
Returns the fullmove clock representing the move number (incremented every time black makes a move)

**Arguments**
None

**Returns**
int

---

```python
Game.fen() -> str
```
Returns the FEN notation of current position

**Arguments**
None

**Returns**
String

---

```python
```

**Arguments**

**Returns**