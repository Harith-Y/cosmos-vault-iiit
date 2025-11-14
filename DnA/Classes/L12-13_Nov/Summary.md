The meeting focused on normalization guidelines and concepts in database design,
emphasizing the importance of functional dependencies and the implications of
prime attributes and candidate keys. Participants discussed the necessity of
achieving First Normal Form (1NF) to avoid anomalies and ensure proper data
structure, while also addressing issues related to partial dependencies that
violate Second Normal Form (2NF). Solutions for design problems were explored,
including the decomposition of schemas to eliminate redundancy and improve
querying efficiency. The discussion extended to Third Normal Form (3NF) and
Boyce-Codd Normal Form (BCNF), highlighting the need for strict compliance to
avoid transitive dependencies. Additionally, an overview of the application
process for a lab was provided, along with project management concerns regarding
time management and departmental collaboration. Next steps included independent
problem-solving on normalization examples and reviewing BCNF concepts through a
video.

**Next steps**
 * Participants to apply normalization concepts in their designs to avoid
   anomalies and ensure proper functional dependencies. (05:16)
 * Participants to explore different table designs for employee and project data
   to optimize database structure. (20:01)
 * Participants to identify functional dependencies violating second normal form
   in the provided schema. (28:31)
 * Participants to solve normalization examples independently after the
   discussion. (50:20)
 * Participants to review a 12-minute video explaining the BCNF concepts
   discussed. (01:02:10)
 * An info session will be held on January 9th post-dinner, lasting 45 minutes
   to 1 hour. (01:07:29)
 * Participants to check the time for the activity submission and confirm the
   status of the candidate key. (01:19:03)

**AI Insights**

The meeting on Functional Dependencies and Normalization demonstrated a mix of
clear next steps and varying levels of engagement among participants. While some
actionable items were identified, there were also segments lacking clarity in
future actions. Engagement levels were generally high, with participants
actively contributing, asking questions, and discussing key concepts, indicating
a strong interest in the subject matter. The meeting adhered to the scheduled
duration, reflecting effective time management. Overall, the sentiment remained
neutral to positive, with constructive discussions and a focus on educational
content.

**Topics & Highlights**
 1.  Normalization Guidelines and Concepts (01:25)
     * **Concern** | Anomalies can occur if relations are not designed properly,
       leading to spurious tuples. (04:17)
     * **Next steps** | Participants to apply normalization concepts in their
       designs to avoid anomalies and ensure proper functional dependencies.
       (05:16)
     * **Fact** | Normalization is the process of decomposing unsatisfactory
       relations to avoid anomalies. (05:47)
     * **Fact** | Functional dependencies are defined as the set of attributes where
       one attribute functionally determines another. (04:41)
       
 2.  Prime Attributes and Candidate Keys (07:01)
     * **Fact** | Prime attributes must be members of candidate keys, while
       non-prime attributes are not. (07:14)
     * **Fact** | First Normal Form (1NF) requires that attributes must not have
       composite or multi-valued attributes. (09:18)
     * **Fact** | Examples of candidate keys include student name and cell number,
       employee number and SSN. (07:42)
     * **Fact** | In the discussed example, A, B, C, D are all prime attributes with
       no non-prime attributes. (08:30)
     * **Fact** | Most RDBMS require relations to be in 1NF for implementation.
       (11:06)
       
 3.  Discussion on Solutions for Design Problem (12:43)
     * **Fact** | Three different solutions to the design problem were discussed,
       including taking data into two tables and creating a design with multiple
       D locations. (15:47)
     * **Concern** | The design solutions may lead to issues such as null values and
       limitations on the number of D locations. (15:05)
       
 4.  Database Normalization and Querying (16:41)
     * **Decision** | The first option for database design is commonly used due to
       limitations in other options. (18:18)
     * **Next steps** | Participants to explore different table designs for employee
       and project data to optimize database structure. (20:01)
     * **Concern** | The complexity of querying with multiple attributes can lead to
       increased processing time. (17:21)
     * **Fact** | Normalization aims to reduce querying time and simplify queries.
       (17:40)
       
 5.  Normalization Concepts and Dependencies (21:51)
     * **Fact** | Discussion on the importance of removing nested relations and
       ensuring attributes are atomic for normalization. (22:25)
     * **Next steps** | Participants to identify functional dependencies violating
       second normal form in the provided schema. (28:31)
     * **Fact** | Explanation of fully functional dependency and partial dependency
       with examples provided. (24:40)
       
 6.  Normalization and Decomposition Discussion (29:25)
     * **Concern** | FD2 and FD3 violate 2NF due to partial dependency issues.
       (29:58)
     * **Decision** | The proposed solution is to break all functional dependencies
       into independent relations. (34:20)
       
 7.  Normalization and Functional Dependencies (34:50)
     * **Fact** | The discussion covers the definitions and requirements for 1NF,
       2NF, and 3NF in database design. (37:07)
     * **Decision** | It was decided to decompose the schema into employee project
       and project to achieve 2NF compliance. (36:51)
     * **Concern** | Concerns were raised about redundancy in storing SSN and P
       number across different tables. (35:52)
       
 8.  Normalization to 3NF (40:54)
     * **Fact** | 3NF requires compliance with 1NF and 2NF, ensuring no non-prime
       attributes are transitively dependent on the primary key. (41:02)
     * **Concern** | Redundancy issues arise when both employee ID and SSN are used
       with names, leading to potential data duplication. (42:54)
     * **Decision** | The proposed design includes separating employee data into two
       relations to eliminate transitivity and redundancy. (45:52)
       
 9.  Normalization Examples and Discussion (46:26)
     * **Fact** | The discussion includes examples of normalization forms,
       specifically 2NF and 3NF, and their requirements. (46:26)
     * **Next steps** | Participants to solve normalization examples independently
       after the discussion. (50:20)
       
 10. Discussion on 2NF and 3NF (52:06)
     * **Fact** | BCNF is the highest form of normalization discussed in the
       meeting. (59:06)
     * **Fact** | The definition of 2NF involves prime attributes, not primary keys.
       (55:23)
       
 11. BCNF Discussion (01:00:06)
     * **Fact** | Area is not a super key of large money, which is a violation of
       BCNF. (01:01:02)
     * **Fact** | BCNF is stronger than 3NF, indicating a stricter normalization
       requirement. (01:01:17)
     * **Next steps** | Participants to review a 12-minute video explaining the BCNF
       concepts discussed. (01:02:10)
       
 12. Application Process Overview (01:06:10)
     * **Fact** | The application task must be submitted within 10 days, followed by
       a technical interview. (01:06:24)
     * **Next steps** | An info session will be held on January 9th post-dinner,
       lasting 45 minutes to 1 hour. (01:07:29)
     * **Fact** | Results will be announced between January 7th and the midterm
       exam. (01:06:28)
       
 13. Project Management Discussion (01:14:13)
     * **Concern** | There are concerns about the project working on multiple
       departments and the time management of submissions. (01:15:04)
     * **Next steps** | Participants to check the time for the activity submission
       and confirm the status of the candidate key. (01:19:03)
       
 14. Discussion on 2NF and BCNF (01:27:37)
     * **Concern** | There is confusion regarding the relationship between 2NF and
       BCNF. (01:36:14)
     * **Fact** | The meeting included discussions about functional dependencies
       (FD) related to BCNF. (01:36:52)
       
