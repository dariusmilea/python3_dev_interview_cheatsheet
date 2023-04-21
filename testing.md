# Software Testing / QA Interview cheat sheet

# Table of contents

1. [Software testing definition](#definition)
2. [Levels](#levels)
3. [Methods](#testing_methods)
4. [Types](#testing_types)
5. [References](#references)

## 1. Software testing definition <a name="definition"></a>

Software Testing is the practice of verifying and validating software to ensure that it meets its specified requirements and behaves as expected.

The main reasons for Software Testing are:

- **Ensuring Quality**: Software Testing helps in ensuring that the software meets quality standards (which is mainly conformance to requirements and expectations).
- **Enhancing User Experience**: Software Testing helps in improving user experience by identifying usability and functionality issues in the software.
- **Compliance**: Software Testing helps in ensuring that the software complies with standards and regulations of the specific industry and reduces the risk of legal issues and financial penalties.
- **Cost Savings**: Software Testing helps in avoiding or lowering costly rework, redesign, and maintenance by identifying defects early in the development process.
  Reputation: Software Testing helps in enhancing the company’s reputation by avoiding embarrassing defects and ensuring high quality software.

**SOFTWARE QUALITY** is the degree of conformance to explicit or implicit requirements and expectations.

**Level** = _WHEN_ to test

**Method** = _HOW_ to test

**Type** = _WHAT_ to test

Explicit: clearly defined and documented

Implicit: not clearly defined and documented but indirectly suggested

Requirements: business/product/software requirements

Expectations: mainly end-user expectations

## 2. Levels <a name="levels"></a>

There are four levels of software testing: Unit >> Integration >> System >> Acceptance.

| Level               | Description                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Unit testing        | A level of the software testing process where individual units of a software are tested. The purpose is to validate that each unit of the software performs as designed.                                                             |
| Integration testing | A level of the software testing process where individual units are combined and tested as a group. The purpose of this level of testing is to expose faults in the interaction between integrated units.                             |
| System testing      | A level of the software testing process where a complete, integrated system is tested. The purpose of this test is to evaluate the system’s compliance with the specified requirements.                                              |
| Acceptance testing  | A level of the software testing process where a system is tested for acceptability. The purpose of this test is to evaluate the system’s compliance with the business requirements and assess whether it is acceptable for delivery. |

## 3. Testing methods <a name="testing_methods"></a>

| Method            | Description                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Static testing    | A method of testing whereby work products are reviewed without executing them.                                                           |
| Dynamic testing   | A method of testing whereby the behavior of work products is evaluated by executing them.                                                |
| Black box testing | A software testing method in which the internal structure/design/implementation of the item being tested is **not** known to the tester. |
| White box testing | A software testing method in which the internal structure/design/implementation of the item being tested is known to the tester.         |
| Gray box testing  | A software testing method which is a combination of Black Box Testing method and White Box Testing method.                               |
| Agile testing     | A method of software testing that follows the principles of agile software development.                                                  |
| Ad Hoc testing    | A method of software testing without any planning and documentation.                                                                     |
| Manual testing    | A method of testing whereby software is tested manually (by a human)                                                                     |
| Automated testing | A method of testing whereby software is tested with the help of scripts and tools.                                                       |

## 4. Testing types <a name="testing_types"></a>

| Type                   | Description                                                                                                                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Functional testing     | Functional Testing is a type of software testing (or a group of software testing types) whereby the system is tested against the functional requirements/ specifications.                             |
| Smoke testing          | Smoke Testing, also known as “Build Verification Testing”, is a type of software testing that comprises of a non-exhaustive set of tests that aim at ensuring that the most important functions work. |
| Regression testing     | Regression testing is a type of software testing that intends to ensure that changes (enhancements or defect fixes) to the software have not adversely affected it.                                   |
| Non-functional testing | Non-functional testing is a group of software testing types whereby the system is tested against the non-functional requirements like usability, performance, security and compliance.                |
| Usability testing      | Usability Testing is a type of software testing done from an end-user’s perspective to determine if the system is easily usable.                                                                      |
| Performance testing    | Performance Testing is a type of software testing that intends to determine how a system performs in terms of responsiveness and stability under a certain load.                                      |
| Security testing       | Security Testing is a type of software testing that intends to uncover vulnerabilities of the system and determine that its data and resources are protected from possible intruders.                 |
| Compliance testing     | Compliance Testing [also known as conformance testing, regulation testing, standards testing] is a type of testing to determine the compliance of a system with internal or external standards.       |

## 5. References <a name="references"></a>

This document was created with the help of the [Software Testing Fundamentals website](https://softwaretestingfundamentals.com/).
