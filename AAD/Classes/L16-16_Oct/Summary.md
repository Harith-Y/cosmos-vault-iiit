The meeting focused on various aspects of NP-Hard problems, including
definitions, examples, and the relationships between different computational
problems. Key discussions included the minimum vertex cover problem, the minimum
word score problem, and the set cover problem, emphasizing their NP-completeness
and the methods for demonstrating this status through reductions. The role of
verifiers in NP and the implications of P versus NP were also explored,
alongside the definitions and significance of Co-NP. Additionally, the
conversation introduced non-deterministic Turing machines (NDTM) and a new
model, non-deterministic decision machines (NDDM), highlighting their acceptance
criteria. Concerns were raised about the practical applications of Co-NP and the
challenges in constructing short certificates for certain problems. The meeting
concluded with plans for future discussions and tasks related to graph theory
and complexity classifications.

**Next steps**
 * Plan to show that word discover is in NP and provide a reduction from set
   cover to word discover. (23:33)
 * Participants to think of ways to utilize the new NDDM model in practical
   applications. (50:34)
 * Participants to construct a graph G5 to demonstrate the relationship between
   vertex cover and satisfiability. (52:47)
 * Next class on October 23rd will not cover new material as per student
   request. (01:19:07)

**AI Insights**

The meeting on NP-Hard Problems demonstrated a mix of engagement and
participation, with multiple speakers actively contributing to technical
discussions. However, there was a notable lack of clarity regarding next steps,
as many actionable items were not defined. The meeting adhered to the scheduled
duration, and the overall sentiment remained neutral, focusing on technical
aspects without emotional language. While the participants were involved in
complex topics, the absence of clear follow-up actions may impact future
progress.

**Topics & Highlights**
 1.  NP-Hard Problem Discussion (05:47)
     * **Fact** | The minimum vertex cover problem was introduced with a specific
       graph example. (10:40)
     * **Fact** | NP-Hard is defined in relation to problems in NP-Hard. (05:47)
     * **Fact** | An example of a 3CF formula and its corresponding gadget G5 was
       discussed. (08:05)
       
 2.  Minimum Word Score Problem (14:34)
     * **Fact** | The minimum word score problem is discussed in relation to its
       NP-completeness and decision version. (14:34)
     * **Concern** | There may be multiple ways to pose optimization problems as
       decision problems, but they must be meaningful. (16:24)
     * **Decision** | The group aims to show that the word discover problem is NP
       complete by demonstrating it is in NP and reducing from a known NP
       complete problem. (19:01)
       
 3.  Set Cover and NP Completeness (21:60)
     * **Fact** | Set cover is NP because a certificate can be quickly checked for
       its validity. (22:47)
     * **Next steps** | Plan to show that word discover is in NP and provide a
       reduction from set cover to word discover. (23:33)
     * **Fact** | Most NP-complete problems have the answer itself as a witness for
       verification. (24:31)
     * **Fact** | The discussion includes the definition of NP and the verification
       process for languages. (27:02)
       
 4.  Discussion on NP and Verifiers (28:44)
     * **Concern** | The challenge of building short certificates for 'sad bar' was
       raised, questioning its membership in NP. (34:09)
     * **Fact** | The discussion includes the definition of NP and the role of
       verifiers in polynomial time. (32:00)
       
 5.  P versus NP Discussion (35:25)
     * **Concern** | There is uncertainty regarding whether NP and co-NP classes are
       the same or not, indicating an ongoing debate in the field. (41:05)
     * **Fact** | The discussion highlights that if a problem is in P, it is also in
       NP, as a verifier with a null certificate acts as a decider. (37:43)
       
 6.  Non-Deterministic Turing Machines (NDTM) (41:19)
     * **Fact** | NDTM accepts an input if there exists one accepting path. (42:25)
     * **Fact** | The complement of an NDTM's acceptance is defined as all paths
       rejecting. (43:11)
     * **Fact** | Co-NP is defined as every path rejecting according to the
       discussed definition. (44:44)
       
 7.  Discussion on Co-NP Definition (45:15)
     * **Concern** | The definition of Co-NP may not be intuitive or useful in
       practical applications. (46:34)
     * **Fact** | Co-NP can be viewed as a short certificate for a 'no' answer in
       computational problems. (48:47)
     * **Fact** | Co-NP is defined as the complement of NP, meaning there exists a
       non-accepting path. (46:10)
       
 8.  Discussion on NDTM and NDDM Models (49:32)
     * **Task** | Participants to construct a graph G5 to demonstrate the
       relationship between vertex cover and satisfiability. (52:47)
     * **Fact** | NDTM accepts W if there is an accepting path; it does not accept W
       if all parts are not accepted. (50:10)
     * **Next steps** | Participants to think of ways to utilize the new NDDM model
       in practical applications. (50:34)
     * **Fact** | The proposed NDDM rejects W if there is a rejecting part,
       introducing a new model concept. (50:29)
       
 9.  Vertex Cover Problem Discussion (56:18)
     * **Fact** | The vertex cover problem involves finding the minimum number of
       vertices that covers all edges in a graph. (01:00:14)
     * **Concern** | There cannot be a vertex cover of size less than 12 plus n due
       to the need to cover edges in triangles. (59:13)
     * **Decision** | The term 'minimum vertex cover' should not be confused with
       'edge cover' as they represent different problems. (01:02:00)
       
 10. Vertex Cover Problem Discussion (01:03:23)
     * **Fact** | Vertex cover is defined as a subset of vertices covering all
       edges, requiring at least 12 vertices for certain configurations.
       (01:03:23)
     * **Fact** | If a vertex cover of size n plus 12 exists, it implies specific
       choices of vertices to cover edges without leaving any uncovered.
       (01:05:21)
     * **Fact** | If there is a vertex cover of size 2n plus n in G5, then the
       propositional formula is satisfied. (01:09:20)
       
 11. Graph Covering and Satisfiability (01:09:57)
     * **Fact** | If phi is satisfiable, then G phi has a word discover of size 12
       percent. (01:11:37)
     * **Fact** | The minimum number of vertices that covers all edges is defined as
       a vertex cover. (01:15:16)
       
 12. Complexity of H Cover and Set Cover (01:16:13)
     * **Next steps** | Next class on October 23rd will not cover new material as
       per student request. (01:19:07)
     * **Fact** | Minimum H cover is in P, indicating its complexity classification.
       (01:17:02)
     * **Concern** | The discussion revealed that proving H cover's reducibility to
       set cover is largely considered unproductive. (01:18:06)
     * **Fact** | Minimum word discover is NP complete, indicating its complexity
       classification. (01:18:42)
       

CREDITS: Asritha Singam