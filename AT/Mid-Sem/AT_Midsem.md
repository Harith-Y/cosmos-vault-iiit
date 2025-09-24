1. Prove set of Strings is countable and set of Languages is uncountable. (Hint: Bijection to Natural Numbers) #Sipser (4.18)
2. Give TM Description for L = { ww | w ∈ {0,1}* }
3. Give the language for the Grammar:
	- S --> aS | bA
	- A --> aA | bB
	- B --> aB | bC
	- C -> aC | ε
4. Prove that the power of Oblivious Turing Machine is the same as that of Turing Machine.
5. Prove / Disprove Collatz Conjecture using A_TM #Sipser (5.31)
6. Prove that Regular TM = {M| M is a regular language} is undecidable using A_TM #Sipser (5.3)
7. Prove whether the below language is regular #Sipser (1.32)
	- Σ_3 = { [ [ 0 ], [ 1 ], [ 1 ] ] }
	- B = {w | w in Σ_3* with sum of top 2 rows = bottom row}
	- Hint: Use B^R where L^R = { w^R | w ∈ L }
8. State whether the following languages are regular or context-free. Draw the corresponding automaton (DFA/PDA) to support your answer.
	1. L1 = {w| |#0′s − #1′s| ≤ 1} 
	2. L2 = {w| |#0′s − #1′s| ≤ 1, ∀ prefixes of w} 
	- Note: The string 00001111 will belong to L1 but not L2 since 00001, a prefix of 00001111, does not satisfy |#0′s − #1′s| ≤ 1.
9. The language L consisting of all strings having an equal number of 0’s and 1’s is context-free. 
	 - L = { w| |#0′s − #1′s| = 0 }
	 - G : S -> 0S1 | 1S0 | SS | e
	 1) Give the smallest length string (In L, other than e) which shows that the Grammar is Ambiguous.
	 2) Formally show that the string provided in part 1 is has ambiguity by drawing parse trees.

### Bonus:
Double-Write TM Problem
