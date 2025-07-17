Zastosowałem przeszukiwanie wszerz, przez co było ono dużo bardziej optymalne czasowo. Teraz problemem jest zużycie RAMu w komputerze, ponieważ program musi pamiętać wiele kombinacji i od nich zaczynać. Koncepcja postrzegania kostki nie zmienia się. 

Tabela będzie predstawiała zużytą pamięć i czas działania programu. Moim głównym zadaniem będzie zmniejszenie czasu działania programu

Czas wykonywania:
| Technika | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| -------- | - | - | - | - | - | - | - | - |
| Czysty BFS   | 0.0 | 0.0007 | 0.0138 | 0.267 | 5.6362 | - | - | - |
| Pomiń jezeli stan się nie zmienia | 0.0 | 0.0006 | 0.0114 | 0.2093 | 4.2118 | - | - | - 
| dodanie bytearray()   | 0.0001 | 0.0006 | 0.0107 | 0.1924 | 4.2696 | - | - | - |
| sprawdzenie tylko jednego przypadku zamiast 3  | 0.0 | 0.0006 | 0.011 | 0.1982 | 4.4777 | 0 | 6                |
| Sytuacje typu (R2, R) i (R,L,R) | 0.0 | 0.0004 | 0.0058 | 0.0727 | 1.1087 | 14.1586 | 24               |
| DR   | 0 | 0 | 1 | 0 | 0 | 1 | 9                |
| DF   | 0 | 1 | 1 | 0 | 0 | 0 | 40               |
| DL   | 0 | 0 | 1 | 0 | 1 | 0 | 10               |
| LB   | 1 | 0 | 0 | 0 | 1 | 0 | 34               |
| RB   | 1 | 0 | 0 | 0 | 0 | 1 | 33               |
| RF   | 0 | 1 | 0 | 0 | 0 | 1 | 17               |
| LF   | 0 | 1 | 0 | 0 | 1 | 0 | 18               |


Zużycie ramu (MB), "-" - out of memory:
| Technika | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| -------- | - | - | - | - | - | - | - | - |
| Czysty BFS   | 43.52 | 43.67 | 45.15 | 71.69 | 580.25 | - | - | - |
| Pomiń jezeli stan się nie zmienia | 43.29 | 43.46 | 44.82 | 65.11 | 454.09 | - | - | - |
| dodanie bytes() | 43.72 | 43.63 | 44.61 | 63.79 | 432.02 | - | - | - |
| sprawdzenie tylko jednego przypadku zamiast 3   | 43.34 | 43.77 | 44.83 | 63.64 | 428.5 | - | - | - |
| Sytuacje typu (R2, R) i (R,L,R) | 43.61 | 43.65 | 44.02 | 50.94 | 136.73 | 1181.71 | - | - |
| DR   | 0 | 0 | 1 | 0 | 0 | 1 | 9                |
| DF   | 0 | 1 | 1 | 0 | 0 | 0 | 40               |
| DL   | 0 | 0 | 1 | 0 | 1 | 0 | 10               |
| LB   | 1 | 0 | 0 | 0 | 1 | 0 | 34               |
| RB   | 1 | 0 | 0 | 0 | 0 | 1 | 33               |
| RF   | 0 | 1 | 0 | 0 | 0 | 1 | 17               |
| LF   | 0 | 1 | 0 | 0 | 1 | 0 | 18               |