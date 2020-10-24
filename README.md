# TicTacToe - The Basic Algorithm


1.	Turn-1: Go(1) (upper left corner)

2.	Turn-2: if Board[5] is blank then Go(5) else Go(1)

3.	Turn-3: if Board[9] is blank then Go(9) else Go(3)

4.	Turn-4: if posswin(X) is not 0, then Go(posswin(X)) else Go(Make2)

5.	Turn-5: if posswin(X) is not 0, then Go(posswin(X)) else if posswin(O) is not 0 then Go(Posswin(O)){i.e. block opponent’s Win; else if Board[7] is blank then       
            Go(7) else Go(3).
            
6.	Turn-6: if posswin(O) is not 0 then Go(Posswin(O)) else if posswin(X) is not 0, then Go(posswin(X)) else Go(make2).

7.	Turn-7: if posswin(X) is not 0, then Go(posswin(X)) else if posswin(O) is not 0 then Go(Posswin(O)) else goanywhere that is blank.

8.	Turn-8: if posswin(O) is not 0 then Go(Posswin(O)) else if posswin(X) is not 0, then Go(posswin(X)) else go anywhere that is blank.

9.	Turn-9: Same as Turn=7. 
