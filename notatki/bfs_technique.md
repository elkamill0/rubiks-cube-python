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
| cofanie się po rodzicach zamiast listy path | 0.0 | 0.0005 | 0.0062 | 0.0734 | 0.9795 | 12.1857 | 9                |
| dodanie __slots__   | 0.0 | 0.0005 | 0.0048 | 0.0624 | 0.8313 | 10.6165 |
| zmiana bfs na dfs   | 0.0 | 0.0005 | 0.0053 | 0.0623 | 0.7397 | 9.6591 | 110.75083
| dfs w c | 0.0 | 0.0 | 0.0005 | 0.0059 | 0.0707 | 0.8665 | 10.6262 | 131.5391 |
| -1 level dfs | 0.0 | 0.0 | 0.0003 | 0.0045 | 0.0560 | 0.6369 | 7.8001 | 95.7645 |
| 5 moves limit before end | 0.0 | 0.0 | 0.0 | 0.0001 | 0.0009 | 0.0114 | 0.1373 | 1.6813 | 60.0913 |
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
| cofanie się po rodzicach zamiast listy path | 43.48 | 43.55 | 43.96 | 48.11 | 99.07 | 725.09 | 9                |
| dodanie __slots__   | 43.37 | 43.62 | 43.73 | 46.97 | 87.5 | 581.0 | 4694.62 |
| zmiana dfs na bfs   | 43.23 | 43.66 | 43.45 | 43.34 | 43.3 | 43.64 | 43.48 |
| dfs w c | 31.68 | 31.68 | 32.01 | 31.57 | 31.88 | 31.87 | 216.25 | 2632.25
| -1 level dfs | 31.59 | 31.68 | 31.84 | 31.89 | 31.80 | 31.80 | 31.76 | 216.00 | - |
| 5 moves limit before end | 31.57 | 31.55 | 31.36 | 31.60 | 31.45 | 31.66 | 31.74 | 31.75 | 181.00 |
| RF   | 0 | 1 | 0 | 0 | 0 | 1 | 17               |
| LF   | 0 | 1 | 0 | 0 | 1 | 0 | 18               |