## Nowy koncept
Nowy koncept skryptu opiera się na pobieraniu samych krawędzi crossa, aby nie obliczać dla wszystkich krawędzi, ponieważ na ten moment nie jest to istotne. Interesują nas tylko ramiona crossa, które powinny znaleźć się po kolei we właściwym miejscu, czyli kiedy określona reprezentacja binarna jest spełniana dla danego pola na kostce.

Kostka wygląda w taki sposób:

Górna wartstwa
| | | |
|-|-|-|
| |36| |
|6| |5|
| |20| |
| |  | |


Środkowa wartstwa
| | | | |
|-|-|-|-|
|34|18|17|33|
|  |  |  |  |


Dolna warstwa
| | | |
|-|-|-|
| |24| |
|10| |9|
| |40| |
| |  | |


Na reprezentację binarną:
| Ruch | B | F | D | U | L | R | Wynik dziesiętny |
| ---- | - | - | - | - | - | - | ---------------- |
| UB   | 1 | 0 | 0 | 1 | 0 | 0 | 36               |
| UR   | 0 | 0 | 0 | 1 | 0 | 1 | 5                |
| UF   | 0 | 1 | 0 | 1 | 0 | 0 | 20               |
| UL   | 0 | 0 | 0 | 1 | 1 | 0 | 6                |
| DB   | 1 | 0 | 1 | 0 | 0 | 0 | 24               |
| DR   | 0 | 0 | 1 | 0 | 0 | 1 | 9                |
| DF   | 0 | 1 | 1 | 0 | 0 | 0 | 40               |
| DL   | 0 | 0 | 1 | 0 | 1 | 0 | 10               |
| LB   | 1 | 0 | 0 | 0 | 1 | 0 | 34               |
| RB   | 1 | 0 | 0 | 0 | 0 | 1 | 33               |
| RF   | 0 | 1 | 0 | 0 | 0 | 1 | 17               |
| LF   | 0 | 1 | 0 | 0 | 1 | 0 | 18               |


## Zakazane ruchy

Koncepcja powstała aby nie wykonywać zbędnych ruchów, które nie przemieszczą ramion crossa na kostce.
Używając funkcję or dla ramion crossa, które zostały zamienione na reprezentację binarną sposowduje że wykorzystując funkcję "or" tam gdzie jest "0", jesteśmy pewni że nie warto wykorzystywać tego ruchu.

### Dla przykładu:
Dla scrambla
`L2 B2 L2 U' B2 L2 U' R2 D' L2 U B2 R B' D F L F2 D F2` mamy nasze ramiona crossa znajdują się w miejscu
```
RB -> 100001
RF -> 010001
UL -> 000110
LF -> 010010
------------
OR    110111
```

Teraz jak przełożymy to na tabelę wyżej otrzymamy
| B | F | D | U | L | R |
| - | - | - | - | - | - |
| 1 | 1 | 0 | 1 | 1 | 1 |

czyli ruch D nic nam nie zmien

ps. Oczywiście wiem że używając ruchów, które nie wskazywałyby na ewaluację krzyża na dole są potrzebne do przygotowania kolejnych par, x-crossów itd., jednak skupiam się na samym optymalizowaniu wyodrębnienia dobrych prypadków crossa.

## Ruchy

Ruchy są zrobione tak, aby każdy ruch zamianiał postać binarną na następną postać binarną. One będą jeszcze dokładnie dopracowywane. Teraz zajmę się robieniem pętli