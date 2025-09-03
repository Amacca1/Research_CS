---
title: 'RAG Pipeline Model Comparison Report with Evaluation Scores'
description: 'Full report.'
pubDate: 'Sep 3 2025'
---


# RAG Pipeline Model Comparison Report with Evaluation Scores

## Executive Summary

This enhanced report integrates LLM judge evaluation scores with the original performance metrics to provide a comprehensive view of model quality beyond just speed and cost.

### Evaluation Criteria

The LLM judge evaluates responses on three key criteria:
- **Cites All Relevant**: Whether the response cites all passages from context that are relevant to the question
- **Not Paraphrasing**: Whether the response quotes verbatim from source documents vs paraphrasing
- **Cites Sections/Paragraphs**: Whether the response properly cites section numbers and paragraph references

## Enhanced Performance Overview

| Model | Success Rate | Avg Time (s) | Total Cost | Cites All | Not Para | Cites Sections | Overall Quality |
|-------|-------------|-------------|------------|-----------|----------|----------------|-----------------|
| Claude Haiku 3.5 | 100.0% | 3.15 | $0.013560 | 0.90 | 0.70 | 0.90 | 0.83 |
| Deepseek | 100.0% | 11.04 | $0.007277 | 0.90 | 0.90 | 0.60 | 0.80 |
| GPT-O3 | 100.0% | 11.54 | $0.021297 | 0.90 | 0.90 | 0.60 | 0.80 |
| Claude Sonnet 4 | 100.0% | 2.73 | $0.048360 | 0.90 | 0.90 | 0.60 | 0.80 |
| Gemini 2.5 Flash | 100.0% | 1.42 | $0.005431 | 0.90 | 0.80 | 0.60 | 0.77 |
| Claude Opus 4.1 | 100.0% | 4.31 | $0.252825 | 0.90 | 0.60 | 0.80 | 0.77 |
| GPT-5 Nano | 100.0% | 12.70 | $0.009882 | 0.80 | 0.80 | 0.50 | 0.70 |
| Gemini 2.5 Pro | 100.0% | 2.34 | $0.030156 | 0.70 | 0.80 | 0.40 | 0.63 |
| GPT-5 | 60.0% | 23.68 | $0.083575 | 0.50 | 0.50 | 0.30 | 0.43 |


## Quality Analysis

### Top Performers by Evaluation Criteria

#### Cites All Relevant Sources

1. **Gemini 2.5 Flash**: 0.90
2. **Deepseek**: 0.90
3. **Claude Haiku 3.5**: 0.90
4. **GPT-O3**: 0.90
5. **Claude Sonnet 4**: 0.90

#### Verbatim Quoting vs Paraphrasing

1. **Deepseek**: 0.90
2. **GPT-O3**: 0.90
3. **Claude Sonnet 4**: 0.90
4. **Gemini 2.5 Flash**: 0.80
5. **GPT-5 Nano**: 0.80

#### Section/Paragraph Citations

1. **Claude Haiku 3.5**: 0.90
2. **Claude Opus 4.1**: 0.80
3. **Gemini 2.5 Flash**: 0.60
4. **Deepseek**: 0.60
5. **GPT-O3**: 0.60


## Detailed Evaluation Results

### Gemini 2.5 Flash - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.90
- Average Not Paraphrasing: 0.80  
- Average Cites Sections: 0.60

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** 4 personnel (Table 2D.1, Section 2D3). *Performance: 0.69s, Cost: $0.000312, Tokens: 898→17* ---...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes the relevant table entry and cites both section and table

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** Key User Requirements (KURs) are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction o...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response quotes the exact definition from snippet 1, but does not cite the specific section. Covers the key points about KURs and their differentiation from other priorities.

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes section 2C2.a and includes verbatim example text

---

### Deepseek - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.90
- Average Not Paraphrasing: 0.90  
- Average Cites Sections: 0.60

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** **2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation ...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes Table 2D.1 and cites section 2D3 correctly

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** a. **Priority.** A priority should be assigned to each element of requirement.¹³    - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service wi...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response directly quotes the definition of KURs from the first snippet. However, it does not cite specific section numbers and does not fully explore the differences with other priorities from the context.

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response quotes the relevant snippet about infrastructure support, but does not cite the specific section number. The quote is verbatim from 2C2a.

---

### GPT-5 Nano - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.80
- Average Not Paraphrasing: 0.80  
- Average Cites Sections: 0.50

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** **2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation ...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✗
- Cites Sections: ✓

**Judge Notes:** Response mentions section 2D3 but does not quote the specific occupancy requirement from Table 2D.1 verbatim

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** a. **Priority.** A priority should be assigned to each element of requirement.¹³    - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service wi...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response uses verbatim text from snippet, but does not cite specific section numbers. Covers most relevant context about KURs.

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** a. **Infrastructure support to the operation.** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp A...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response matches verbatim text from section 2C2a and provides precise examples

---

### Claude Haiku 3.5 - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.90
- Average Not Paraphrasing: 0.70  
- Average Cites Sections: 0.90

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** According to Table 2D.1 in section 2D3, the recommended occupancy for junior ranks is 4 personnel. *Performance: 1.08s, Cost: $0.000909, Tokens: 976→32* ---...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response perfectly matches the table entry in section 2D3, with precise citation

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** According to section 2.a of the context, Key User Requirements (KURs) are defined as: "Key User Requirements (KURs), are the Critical Success Factors without which the facility/service w...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes the definition from section 2.a and explains the distinction between KURs and other priorities

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** According to section 2C2(a), the TIDD should explain what infrastructure is required to support the operation. Specific examples provided include: - 'RSOI camp for 5,000' - 'APOD for Sp ...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes section 2C2(a) and includes verbatim examples, fully addressing the question

---

### GPT-O3 - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.90
- Average Not Paraphrasing: 0.90  
- Average Cites Sections: 0.60

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** **2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation ...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes Table 2D.1 and references section 2D3 and 2D4 appropriately

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** a. **Priority.** A priority should be assigned to each element of requirement.¹³    - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service wi...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response directly quotes the definition of KURs from the first snippet. However, it does not cite specific section numbers and does not fully explore the differences with other priorities using verbatim quotes.

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** a. **Infrastructure support to the operation.** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp A...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response exactly matches the text in section 2C2a and provides verbatim quote with correct citation

---

### Gemini 2.5 Pro - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.70
- Average Not Paraphrasing: 0.80  
- Average Cites Sections: 0.40

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** 4 personnel (2D3, Table 2D.1) *Performance: 1.03s, Cost: $0.001871, Tokens: 898→15* ---...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes the relevant table entry and cites the correct section and table

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** A priority should be assigned to each element of requirement.¹³    - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly b...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response directly quotes the relevant snippet about KURs, but does not cite specific section numbers. The response matches the source text almost verbatim.

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes section 2C2.a and includes verbatim text from the snippet

---

### Claude Sonnet 4 - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.90
- Average Not Paraphrasing: 0.90  
- Average Cites Sections: 0.60

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** According to Table 2D.1, for junior ranks (Ser (a)), the occupancy is 4 personnel. *Performance: 1.61s, Cost: $0.003378, Tokens: 976→30* ---...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes the relevant table entry and cites the section number

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** From the context, here is the relevant passage verbatim: "Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for p...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response quotes the relevant passage verbatim from DOC_1_SNIPPET, but does not cite any section numbers. Covers the definition and distinction of KURs from other priorities.

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** From section 2C2.a: "Infrastructure support to the operation. The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an ...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes section 2C2.a and captures the key requirements for TIDD infrastructure support

---

### Claude Opus 4.1 - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.90
- Average Not Paraphrasing: 0.60  
- Average Cites Sections: 0.80

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** According to Table 2D.1, the occupancy for junior ranks is 4 personnel. Source: Section 2D3, Table 2D.1 – Planning guidelines for the provision of new domestic facilities *Performance: 2...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response perfectly matches the table entry and cites the correct section and table

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** Based on the context provided: **Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good ...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response quotes the exact definition from snippet 1, but does not cite the section number. Covers the key points about KURs and their differentiation from other priorities.

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** According to the document, the Theatre Infrastructure Development Directive (TIDD) should address infrastructure support to the operation by explaining what infrastructure is required to...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes and cites section 2C2.a, covers the key points about infrastructure support from the TIDD directive

---

### GPT-5 - Detailed Evaluation

**Evaluation Summary:**
- Successful Evaluations: 10/10
- Average Cites All Relevant: 0.50
- Average Not Paraphrasing: 0.50  
- Average Cites Sections: 0.30

**Sample Evaluated Responses:**

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?...

**Response:** **Response:** **2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation ...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes Table 2D.1 and references section 2D3 correctly

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?...

**Response:** **Response:** a. **Priority.** A priority should be assigned to each element of requirement.¹³    - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service wi...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✗

**Judge Notes:** Response directly quotes the definition of KURs from the first snippet. However, it does not cite specific section numbers and uses the exact text from the source.

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure...

**Response:** **Response:** **2C2. Contents of a Theatre Infrastructure Development Directive.** The size and contents of the TIDD will vary over time. As a guide it should address: a. **Infrastructure support to t...

**Evaluation Scores:**
- Cites All Relevant: ✓
- Not Paraphrasing: ✓
- Cites Sections: ✓

**Judge Notes:** Response directly quotes section 2C2 and provides verbatim examples of infrastructure support requirements

---


## Original Performance Report

## Detailed Results by Model

### Gemini 2.5 Flash

- **Success Rate:** 100.0%
- **Average Response Time:** 1.42 seconds
- **Total Cost:** $0.005431
- **Errors:** 0/10
- **Notes:** Lightweight Google API

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

4 personnel (Table 2D.1, Section 2D3).


*Performance: 0.69s, Cost: $0.000312, Tokens: 898→17*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

Key User Requirements (KURs) are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).  Any other priority is coded P1, P2 (and so on) to reflect lower priorities. (Source: data/chapter2.md, section a)


*Performance: 1.08s, Cost: $0.000453, Tokens: 751→91*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'. (2C2.a)


*Performance: 2.12s, Cost: $0.000412, Tokens: 822→66*

---

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Response:**

**2C6. Contents of an Infrastructure Development Plan.** Any appropriate format may be used, however, the Infrastructure Development Plan should contain:

a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost. (2C6)

a. **Plan the detailed development of the operational estate.**
   1. Produce infrastructure development plans that are in-tune with the operational plan and Theatre Infrastructure Development Directive. (2D)


*Performance: 2.70s, Cost: $0.000914, Tokens: 813→268*

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Response:**

I don't know.  The provided text discusses the planning and management of military infrastructure, including occupancy guidelines (2D3, Table 2D.1), but does not specify any approval processes required before occupation.


*Performance: 0.97s, Cost: $0.000406, Tokens: 971→46*

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Response:**

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it. The User Requirement Document will record a number of key features:


*Performance: 2.49s, Cost: $0.000984, Tokens: 864→290*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time. (Source: data/chapter2.md)


*Performance: 0.88s, Cost: $0.000458, Tokens: 1017→61*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)? (2C2.b)


*Performance: 0.92s, Cost: $0.000418, Tokens: 836→67*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

248. Changing the Requirement. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.


*Performance: 0.92s, Cost: $0.000426, Tokens: 853→68*

---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Response:**

b. **Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel. (Source: data/chapter2.md, section b)

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time. (Source: data/chapter2.md, section c)


*Performance: 1.39s, Cost: $0.000649, Tokens: 905→151*

---


### Deepseek

- **Success Rate:** 100.0%
- **Average Response Time:** 11.04 seconds
- **Total Cost:** $0.007277
- **Errors:** 0/10
- **Notes:** Chinese API

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

**2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation is not minimum military requirement. Table 2D.1 gives the planning guidance for the provision of new domestic facilities.

| Ser | Personnel | Occupancy |
|-----|-----------|-----------|
| (a) | Junior ranks | 4 personnel |
| (b) | Senior ranks | 4-2 personnel |
| (c) | Junior officers | 4-2 personnel |
| (d) | Senior officers | 1-2 personnel |
| (e) | Command appointments | Single rooms |

**Table 2D.1 – Planning guidelines for the provision of new domestic facilities**

*Performance: 11.11s, Cost: $0.000748, Tokens: 856→160*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

a. **Priority.** A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.

*Performance: 8.35s, Cost: $0.000579, Tokens: 740→98*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'. (Source: data/chapter2.md, 2C2a)

*Performance: 7.31s, Cost: $0.000574, Tokens: 815→70*

---

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Response:**

An Infrastructure Development Plan should contain:

a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost.

Source: data/chapter2.md, section 2C6 and 2C6.d

*Performance: 14.61s, Cost: $0.000810, Tokens: 793→218*

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Response:**

I don't know.

*Performance: 3.57s, Cost: $0.000543, Tokens: 955→5*

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Response:**

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it. The User Requirement Document will record a number of key features:

*Performance: 17.43s, Cost: $0.000963, Tokens: 849→290*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time. (Source: data/chapter2.md, section c)

*Performance: 5.92s, Cost: $0.000632, Tokens: 969→53*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

**2C2. Contents of a Theatre Infrastructure Development Directive.** The size and contents of the TIDD will vary over time. As a guide it should address:

b. **Planning horizon.** The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*Performance: 9.06s, Cost: $0.000634, Tokens: 833→100*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

**248.** **Changing the Requirement.** Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*Performance: 15.15s, Cost: $0.000832, Tokens: 832→218*

---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Response:**

b. **Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

a. **Plan for the base's capability.** By not considering the military capability required at a base, planners will usually under-estimate a Force's reliance on infrastructure. For example, they may assume that weapons and ammunition will be permanently held on vehicles or by personnel, however, a few months into the deployment, the requirement for a magazine and armoury will become apparent. Other facilities typically over-looked are: kitchen and refrigerated food storage, vehicle repair facilities, ranges, parking, entry control point facilities and communications masts. Similarly, planners will often give an arbitrary size of a camp or base determined largely on strategic considerations rather than a manpower estimate against task lines, for example, 'we need a 100-man base at this location'. This invariably leads to an under-estimate in base size.

*Performance: 17.85s, Cost: $0.000961, Tokens: 867→283*

---


### GPT-5 Nano

- **Success Rate:** 100.0%
- **Average Response Time:** 12.70 seconds
- **Total Cost:** $0.009882
- **Errors:** 0/10
- **Notes:** Low Level OpenAI API

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

**2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation is not minimum military requirement. Table 2D.1 gives the planning guidance for the provision of new domestic facilities.

*Performance: 13.32s, Cost: $0.001045, Tokens: 867→2503*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

a. **Priority.** A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.

*Performance: 8.60s, Cost: $0.000669, Tokens: 747→1580*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

a. **Infrastructure support to the operation.** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'.

*Performance: 9.42s, Cost: $0.000761, Tokens: 813→1801*

---

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Response:**

2C6. Contents of an Infrastructure Development Plan. Any appropriate format may be used, however, the Infrastructure Development Plan should contain:

a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost.

*Performance: 21.78s, Cost: $0.001669, Tokens: 809→4072*

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Response:**

b. **Military works area.** A military works area defines the geographic boundaries within which the needs of operational imperatives may be balanced against other regulatory obligations, for example, operational risk may be taken. The boundary of a military works area will usually be coincident with the joint operations area (JOA). Only PJHQ can establish and disestablish a military works area.³ During the life of a military works area there is likely to be a migration from a policy of hastily provided operationally essential infrastructure having a short life and probably incorporating a degree of risk, towards longer lasting infrastructure which is more compliant with UK Health and Safety standards and other statutory obligations. The path and pace of this migration must remain the responsibility of the operational commander, advised by his Infrastructure Staff. Migration may not be homogenous across all areas of a military works area; the commander and his Infrastructure Staff will need to be very clear about what risks can be taken in each part of the military works area.

*Performance: 13.20s, Cost: $0.000950, Tokens: 966→2255*

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Response:**

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it. The User Requirement Document will record a number of key features:

*Performance: 12.57s, Cost: $0.001008, Tokens: 864→2412*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

*Performance: 7.36s, Cost: $0.000635, Tokens: 973→1467*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*Performance: 9.69s, Cost: $0.000709, Tokens: 832→1668*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*Performance: 5.92s, Cost: $0.000479, Tokens: 844→1092*

---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Response:**

b. **Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.

| Ser | Military | Contractors | Ratio | Remarks |
|-----|----------|-------------|--------|---------|
| (a) | 4,200 | 2,400 | 1:1.75 | 530 UK-based contractors, 110 Third Country nationals, 790 Locally recruited workers |
| (b) | 8,000 | 3,200 | 1:2.5 | |

**Table 2.1 – Contractors as a proportion of the force**

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

---
**246.** **Avoid under-estimating the requirement.** Avoid under-estimating the requirement as changes are difficult to accommodate.

a. **Plan for the base's capability.** By not considering the military capability required at a base, planners will usually under-estimate a Force's reliance on infrastructure. For example, they may assume that weapons and ammunition will be permanently held on vehicles or by personnel, however, a few months into the deployment, the requirement for a magazine and armoury will become apparent. Other facilities typically over-looked are: kitchen and refrigerated food storage, vehicle repair facilities, ranges, parking, entry control point facilities and communications masts. Similarly, planners will often give an arbitrary size of a camp or base determined largely on strategic considerations rather than a manpower estimate against task lines, for example, 'we need a 100-man base at this location'. This invariably leads to an under-estimate in base size.

*Performance: 25.13s, Cost: $0.001956, Tokens: 883→4779*

---


### Claude Haiku 3.5

- **Success Rate:** 100.0%
- **Average Response Time:** 3.15 seconds
- **Total Cost:** $0.013560
- **Errors:** 0/10
- **Notes:** Low level Anthropic API

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

According to Table 2D.1 in section 2D3, the recommended occupancy for junior ranks is 4 personnel.

*Performance: 1.08s, Cost: $0.000909, Tokens: 976→32*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

According to section 2.a of the context, Key User Requirements (KURs) are defined as:

"Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs)."

In contrast, other priorities are coded as P1, P2, and so on to reflect lower priorities. KURs are considered the most critical requirements that are essential for the facility or service to be functional, while other priorities are ranked in descending order of importance.

*Performance: 2.65s, Cost: $0.001244, Tokens: 825→146*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

According to section 2C2(a), the TIDD should explain what infrastructure is required to support the operation. Specific examples provided include:
- 'RSOI camp for 5,000'
- 'APOD for Sp Ac and 24 Typhoon aircraft'
- 'up to 20 company-sized patrol bases'

*Performance: 1.89s, Cost: $0.001053, Tokens: 896→84*

---

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Response:**

Based on the context provided, an Infrastructure Development Plan is a document that outlines the development and management of a site's infrastructure. According to section 2C6, it should contain the following key elements:

a. **Description of the estate** (2C6a): A brief outline of the site's role, function, and components of the UK's operational estate.

b. **Ownership** (2C6b): Clearly state the boundaries of UK responsibility, clarify land ownership, and establish who is responsible for infrastructure provision, operation, maintenance, and repair.

c. **Planning horizon** (2C6c): Provide a working assumption of the site's likely tenure, derived from the TIDD and adjusted by local plans.

d. **Planned development work** (2C6d): Show site development plans over time, including:
- Site plans illustrating planned development
- A list of major projects
- Estimated time and cost for these projects

Additionally, section 2C7 notes that Infrastructure Development Plans should:
- Be kept under constant review
- Be re-issued periodically
- Be endorsed by PJHQ
- Help shape the next Theatre Infrastructure Development Directive (TIDD)

*Performance: 4.47s, Cost: $0.001757, Tokens: 866→266*

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Response:**

Based on the provided context, I cannot find a direct answer about specific approvals required before occupation of a military facility. The context discusses infrastructure planning guidelines, occupancy rates, and military works areas, but does not explicitly outline pre-occupation approval processes. To provide a definitive answer about required approvals, I would need additional documentation.

The closest relevant information is in section 204, which suggests that military commanders are responsible for determining infrastructure policy and risk assessments, and in section 2D4, which indicates that any variations from standard guidelines must be explicitly stated in the Tactical Infrastructure Recce Report. However, this does not constitute a comprehensive approval process.

*Performance: 3.50s, Cost: $0.001386, Tokens: 1038→139*

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Response:**

Based on paragraph 242, the Statement of Need (SON) serves the following purposes:

1. To clarify the requirement for infrastructure support
2. Is raised by the unit or organization requiring new infrastructure (the user or sponsor)
3. Helps identify what is actually needed, not just what is wanted
4. Can be expanded into a more detailed User Requirement Document (URD)
5. Provides a basis for documenting and assessing infrastructure requirements

The document specifically notes that the Statement of Need is "in common use" in military organizations, and is typically used to capture the initial infrastructure requirement. An example format for creating a Statement of Need is referenced in Annex 2A of the document.

The paragraph emphasizes the importance of focusing on identifying the actual need, stating: "it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project."

*Performance: 4.30s, Cost: $0.001519, Tokens: 914→197*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

According to section c under the context, bases should be capable of accommodating 125% of their design capacity for a limited period of time to allow for surges during emergencies or rotations. Specifically, the text states: "As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time."

*Performance: 2.04s, Cost: $0.001174, Tokens: 1082→77*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

According to section 2C2(b), the TIDD should:

"give the planning horizon for infrastructure investements throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?"

Additionally, section 2C(c) reinforces this by stating the need to "Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans."

*Performance: 2.31s, Cost: $0.001214, Tokens: 903→123*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

Based on section 248 of the document, a Variation Order (VO) is used when there is a need to change a project requirement midway through construction. Specifically, the document states that when it becomes clear that the original requirement is incomplete or has changed, a project engineer will obtain the cost of the change and note it on a Variation Order. 

The key points about a Variation Order are:
1. It documents changes to the original project requirement
2. The project engineer calculates the cost of the change
3. Work on a Variation Order should not begin without confirming adequate financing
4. A record must be kept explaining the reasons for the requirement change

The document also cautions that most project delays stem from user-initiated changes during construction and a lack of change control, so such variations should be carefully considered.

*Performance: 4.01s, Cost: $0.001450, Tokens: 918→179*

---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Response:**

Based on the context, here are the key factors to consider when planning for base population and contractor presence:

1. Total Population Consideration (Section b):
"Military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked." The context provides a table (Table 2.1) showing the ratio of military personnel to contractors, which ranges from 1:1.75 to 1:2.5, including:
- UK-based contractors
- Third Country nationals
- Locally recruited workers

2. Surge Capacity (Section c):
"Bases should be capable of accommodating 125% of the design capacity for a limited period of time" to allow for emergencies or rotation.

3. Avoid Underestimating Requirements (Section 246a):
Planners should consider:
- Military capability requirements
- Infrastructure needs beyond personnel numbers
- Facilities like:
  * Magazines and armories
  * Kitchen and food storage
  * Vehicle repair facilities
  * Ranges
  * Parking
  * Entry control points
  * Communication masts

4. Experience-Based Planning (Section 228):
Rely on personnel who have recent experience building similar infrastructure in similar locations.

*Performance: 5.22s, Cost: $0.001854, Tokens: 962→271*

---


### GPT-O3

- **Success Rate:** 100.0%
- **Average Response Time:** 11.54 seconds
- **Total Cost:** $0.021297
- **Errors:** 0/10
- **Notes:** New API to test

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

**2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation is not minimum military requirement. Table 2D.1 gives the planning guidance for the provision of new domestic facilities.

**2D4. Variations.** The Tactical Infrastructure Recce Report will explicitly state whether any variations are permitted from those laid out in this document.

| Ser | Personnel | Occupancy |
|-----|-----------|-----------|
| (a) | Junior ranks | 4 personnel |
| (b) | Senior ranks | 4-2 personnel |
| (c) | Junior officers | 4-2 personnel |
| (d) | Senior officers | 1-2 personnel |
| (e) | Command appointments | Single rooms |

**Table 2D.1 – Planning guidelines for the provision of new domestic facilities**

*Performance: 15.43s, Cost: $0.003027, Tokens: 867→1297*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

a. **Priority.** A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.

*Performance: 9.98s, Cost: $0.001887, Tokens: 747→757*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

a. **Infrastructure support to the operation.** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'.

*Performance: 7.15s, Cost: $0.001208, Tokens: 813→401*

---

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Response:**

**2C6. Contents of an Infrastructure Development Plan.** Any appropriate format may be used, however, the Infrastructure Development Plan should contain:

a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost.

*Performance: 21.45s, Cost: $0.003318, Tokens: 809→1457*

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Response:**

I don't know

*Performance: 6.72s, Cost: $0.001037, Tokens: 966→277*

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Response:**

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it. The User Requirement Document will record a number of key features:

*Performance: 12.74s, Cost: $0.003354, Tokens: 864→1461*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

*Performance: 10.13s, Cost: $0.001391, Tokens: 973→452*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

b. **Planning horizon.** The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*Performance: 11.62s, Cost: $0.002376, Tokens: 832→980*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

**248.** **Changing the Requirement.** Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*Performance: 9.36s, Cost: $0.002052, Tokens: 844→815*

---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Response:**

• Count everyone, not just soldiers – include civilian contractors plus any MOD or other-government-department personnel (data/chapter2.md, b. “Consider the total population”).  

• Use recent operational ratios as a guide (e.g., 4 200 military : 2 400 contractors or 8 000 : 3 200) to size facilities for contractor presence (Table 2.1, data/chapter2.md).  

• Design the base to handle short-term surges of up to 125 % of its nominal capacity for emergencies or rotations (data/chapter2.md, c. “Allow for surges”).  

• Avoid under-estimating needs: plan for all supporting infrastructure (magazines, kitchens, workshops, parking, entry control points, comms masts, etc.) instead of fixing an arbitrary camp size (data/chapter2.md, §246 a. “Plan for the base's capability”).

*Performance: 10.83s, Cost: $0.001646, Tokens: 883→602*

---


### Gemini 2.5 Pro

- **Success Rate:** 100.0%
- **Average Response Time:** 2.34 seconds
- **Total Cost:** $0.030156
- **Errors:** 0/10
- **Notes:** Google's API

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

4 personnel (2D3, Table 2D.1)


*Performance: 1.03s, Cost: $0.001871, Tokens: 898→15*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.


*Performance: 2.16s, Cost: $0.002596, Tokens: 751→95*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'. (2C2.a)


*Performance: 2.63s, Cost: $0.002366, Tokens: 822→66*

---

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Response:**

2C6. Contents of an Infrastructure Development Plan. Any appropriate format may be used, however, the Infrastructure Development Plan should contain:

a. Description of the estate. An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. Ownership. It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. Planning horizon. Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. Planned development work. The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost.


*Performance: 2.82s, Cost: $0.004249, Tokens: 813→218*

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Response:**

I don't know.


*Performance: 1.95s, Cost: $0.001908, Tokens: 971→7*

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Response:**

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it. The User Requirement Document will record a number of key features:


*Performance: 3.74s, Cost: $0.005245, Tokens: 864→290*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time. (data/chapter2.md)


*Performance: 2.76s, Cost: $0.002644, Tokens: 1017→59*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)? (2C2. b)


*Performance: 1.73s, Cost: $0.002405, Tokens: 836→67*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement. (248)


*Performance: 3.06s, Cost: $0.004349, Tokens: 853→220*

---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Response:**

Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.


*Performance: 1.55s, Cost: $0.002522, Tokens: 905→66*

---


### Claude Sonnet 4

- **Success Rate:** 100.0%
- **Average Response Time:** 2.73 seconds
- **Total Cost:** $0.048360
- **Errors:** 0/10
- **Notes:** Medium level Anthropic API

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

According to Table 2D.1, for junior ranks (Ser (a)), the occupancy is 4 personnel.

*Performance: 1.61s, Cost: $0.003378, Tokens: 976→30*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

From the context, here is the relevant passage verbatim:

"Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
- Any other priority is coded P1, P2 (and so on) to reflect lower priorities."

*Performance: 2.00s, Cost: $0.004005, Tokens: 825→102*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

From section 2C2.a:

"Infrastructure support to the operation. The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'."

*Performance: 1.89s, Cost: $0.003978, Tokens: 896→86*

---

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Response:**

From section 2C6, an Infrastructure Development Plan should contain these key elements:

"a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost."

Additionally, from section 2C7:

"As with the TIDD, Infrastructure Development Plans should be kept under constant review and be re-issued on a periodic basis. Infrastructure Development Plans should be endorsed by PJHQ. Each iteration helps shape the next TIDD."

*Performance: 3.84s, Cost: $0.006858, Tokens: 866→284*

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Response:**

From the provided context, I cannot find a specific passage that directly addresses what approvals are required before occupying a military facility. While the text discusses Military Works Areas, infrastructure management, and reconnaissance requirements, it does not explicitly state the approval process for facility occupation.

*Performance: 2.07s, Cost: $0.003954, Tokens: 1038→56*

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Response:**

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it.

*Performance: 4.95s, Cost: $0.007137, Tokens: 914→293*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

"Allow for surges. The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time."

*Performance: 1.53s, Cost: $0.004026, Tokens: 1082→52*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

b. **Planning horizon.** The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*Performance: 1.69s, Cost: $0.003789, Tokens: 903→72*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

**248.** **Changing the Requirement.** Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*Performance: 4.77s, Cost: $0.006354, Tokens: 918→240*

---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Response:**

b. **Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

*Performance: 2.97s, Cost: $0.004881, Tokens: 962→133*

---


### Claude Opus 4.1

- **Success Rate:** 100.0%
- **Average Response Time:** 4.31 seconds
- **Total Cost:** $0.252825
- **Errors:** 0/10
- **Notes:** High level Anthropic API

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

According to Table 2D.1, the occupancy for junior ranks is 4 personnel.

Source: Section 2D3, Table 2D.1 – Planning guidelines for the provision of new domestic facilities

*Performance: 2.50s, Cost: $0.018390, Tokens: 976→50*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

Based on the context provided:

**Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).**

**Any other priority is coded P1, P2 (and so on) to reflect lower priorities.**

Source: data/chapter2.md, Section a. **Priority**

*Performance: 3.48s, Cost: $0.020775, Tokens: 825→112*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

According to the document, the Theatre Infrastructure Development Directive (TIDD) should address infrastructure support to the operation by explaining what infrastructure is required to support the operation. Examples given include:
- An 'RSOI camp for 5,000'
- An 'APOD for Sp Ac and 24 Typhoon aircraft'
- 'Up to 20 company-sized patrol bases'

Source: Section 2C2.a

*Performance: 3.44s, Cost: $0.021165, Tokens: 896→103*

---

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Response:**

Based on the context provided, an Infrastructure Development Plan is a planning document that details the development of operational estate infrastructure. 

According to **Section 2C6**, the Infrastructure Development Plan should contain the following key elements:

a. **Description of the estate** - "An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate."

b. **Ownership** - "It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair."

c. **Planning horizon** - "Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans."

d. **Planned development work** - "The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost."

According to **Section 2C7**, "Infrastructure Development Plans should be kept under constant review and be re-issued on a periodic basis. Infrastructure Development Plans should be endorsed by PJHQ. Each iteration helps shape the next TIDD."

*Performance: 6.61s, Cost: $0.036015, Tokens: 866→307*

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Response:**

I don't know. The provided context does not contain information about what approvals might be required before occupation of a military facility. The context discusses planning guidelines for domestic facilities, risk management in military works areas, and information needs for reconnaissance, but does not specify approval requirements for facility occupation.

*Performance: 3.24s, Cost: $0.020145, Tokens: 1038→61*

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Response:**

Based on the context provided:

The Statement of Need (SON) serves to clarify the requirement for any infrastructure support. The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need. The purpose is to identify what is actually needed rather than what is wanted.

The Statement of Need can be expanded upon to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). The URD provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the URD, each element of requirement should be assigned a serial number, describe the requirement in output terms, articulate the standard required, and state what effect is required. It should explain how the infrastructure will be used, allowing designers to determine the best way to achieve it.

Source: Section 242 - Statement of Need and User Requirement Document

*Performance: 4.79s, Cost: $0.028185, Tokens: 914→193*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

Based on the context provided:

**Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

Source: Section 246.c from data/chapter2.md

*Performance: 3.33s, Cost: $0.021855, Tokens: 1082→75*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

Based on the context provided:

The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

Source: Section 2C2.b

*Performance: 3.21s, Cost: $0.019695, Tokens: 903→82*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

Based on the context provided, a Variation Order (VO) is a document used when there is a change to the original requirement during a military infrastructure project. 

According to Section 248 "Changing the Requirement," when a change to the project requirement is needed, "the project engineer will obtain the cost and note it on a Variation Order (VO)." The section further states that "Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs."

A VO is typically used when it becomes clear that the original requirement was incomplete or has changed since project inception, making the facility potentially unfit-for-purpose once completed. It documents the cost implications of the change and ensures proper financial authorization before proceeding with any variation work.

*Performance: 5.54s, Cost: $0.026445, Tokens: 918→169*

---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Response:**

Based on the context provided, the following factors should be considered when planning for base population and contractor presence:

**Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.

**Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

**Plan for the base's capability.** By not considering the military capability required at a base, planners will usually under-estimate a Force's reliance on infrastructure. For example, they may assume that weapons and ammunition will be permanently held on vehicles or by personnel, however, a few months into the deployment, the requirement for a magazine and armoury will become apparent. Other facilities typically over-looked are: kitchen and refrigerated food storage, vehicle repair facilities, ranges, parking, entry control point facilities and communications masts. Similarly, planners will often give an arbitrary size of a camp or base determined largely on strategic considerations rather than a manpower estimate against task lines, for example, 'we need a 100-man base at this location'. This invariably leads to an under-estimate in base size.

(Source: Sections 246.b, 246.c, and 246.a)

*Performance: 6.97s, Cost: $0.040155, Tokens: 962→343*

---


### GPT-5

- **Success Rate:** 60.0%
- **Average Response Time:** 23.68 seconds
- **Total Cost:** $0.083575
- **Errors:** 4/10
- **Notes:** Standard OpenAI API

#### Complete Responses

**Query 1:** What is the recommended occupancy for junior ranks according to Table 2D.1?

**Response:**

**2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation is not minimum military requirement. Table 2D.1 gives the planning guidance for the provision of new domestic facilities.

| Ser | Personnel | Occupancy |
|-----|-----------|-----------|
| (a) | Junior ranks | 4 personnel |
| (b) | Senior ranks | 4-2 personnel |
| (c) | Junior officers | 4-2 personnel |
| (d) | Senior officers | 1-2 personnel |
| (e) | Command appointments | Single rooms |

**Table 2D.1 – Planning guidelines for the provision of new domestic facilities**

*Performance: 15.95s, Cost: $0.015574, Tokens: 867→1449*

---

**Query 2:** What are Key User Requirements (KURs) and how do they differ from other priorities?

**Response:**

a. **Priority.** A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.

*Performance: 16.85s, Cost: $0.011614, Tokens: 747→1068*

---

**Query 3:** What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

**Response:**

**2C2. Contents of a Theatre Infrastructure Development Directive.** The size and contents of the TIDD will vary over time. As a guide it should address:

a. **Infrastructure support to the operation.** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'.

*Performance: 45.52s, Cost: $0.020636, Tokens: 813→1962*

---

**Query 7:** How should surge capacity be considered when sizing military bases?

**Response:**

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

*Performance: 9.20s, Cost: $0.008206, Tokens: 973→699*

---

**Query 8:** What guidance should a TIDD provide about the planning horizon for infrastructure investments?

**Response:**

b. **Planning horizon.** The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*Performance: 18.98s, Cost: $0.012030, Tokens: 832→1099*

---

**Query 9:** What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

**Response:**

**248.** **Changing the Requirement.** Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*Performance: 35.56s, Cost: $0.015515, Tokens: 844→1446*

---

#### Errors Encountered

**Query 4:** What is an Infrastructure Development Plan and what key elements should it include?

**Error:** HTTPSConnectionPool(host='api.openai.com', port=443): Read timed out. (read timeout=60)

---

**Query 5:** What approvals might be required before occupation of a military facility?

**Error:** HTTPSConnectionPool(host='api.openai.com', port=443): Read timed out. (read timeout=60)

---

**Query 6:** What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

**Error:** API error: 404 - {
    "error": {
        "message": "Your organization must be verified to use the model `gpt-5`. Please go to: https://platform.openai.com/settings/organization/general and click on Verify Organization. If you just verified, it can take up to 15 minutes for access to propagate.",
        "type": "invalid_request_error",
        "param": null,
        "code": "model_not_found"
    }
}


---

**Query 10:** What factors should be considered when planning for base population and contractor presence?

**Error:** HTTPSConnectionPool(host='api.openai.com', port=443): Read timed out. (read timeout=60)

---


## Response Comparison by Query

This section shows how each model responded to the same queries for direct comparison.

### Query 1: What is the recommended occupancy for junior ranks according to Table 2D.1?

#### Gemini 2.5 Flash

4 personnel (Table 2D.1, Section 2D3).


*0.69s, $0.000312, 898→17 tokens*

#### Deepseek

**2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation is not minimum military requirement. Table 2D.1 gives the planning guidance for the provision of new domestic facilities.

| Ser | Personnel | Occupancy |
|-----|-----------|-----------|
| (a) | Junior ranks | 4 personnel |
| (b) | Senior ranks | 4-2 personnel |
| (c) | Junior officers | 4-2 personnel |
| (d) | Senior officers | 1-2 personnel |
| (e) | Command appointments | Single rooms |

**Table 2D.1 – Planning guidelines for the provision of new domestic facilities**

*11.11s, $0.000748, 856→160 tokens*

#### GPT-5 Nano

**2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation is not minimum military requirement. Table 2D.1 gives the planning guidance for the provision of new domestic facilities.

*13.32s, $0.001045, 867→2503 tokens*

#### Claude Haiku 3.5

According to Table 2D.1 in section 2D3, the recommended occupancy for junior ranks is 4 personnel.

*1.08s, $0.000909, 976→32 tokens*

#### GPT-O3

**2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation is not minimum military requirement. Table 2D.1 gives the planning guidance for the provision of new domestic facilities.

**2D4. Variations.** The Tactical Infrastructure Recce Report will explicitly state whether any variations are permitted from those laid out in this document.

| Ser | Personnel | Occupancy |
|-----|-----------|-----------|
| (a) | Junior ranks | 4 personnel |
| (b) | Senior ranks | 4-2 personnel |
| (c) | Junior officers | 4-2 personnel |
| (d) | Senior officers | 1-2 personnel |
| (e) | Command appointments | Single rooms |

**Table 2D.1 – Planning guidelines for the provision of new domestic facilities**

*15.43s, $0.003027, 867→1297 tokens*

#### Gemini 2.5 Pro

4 personnel (2D3, Table 2D.1)


*1.03s, $0.001871, 898→15 tokens*

#### Claude Sonnet 4

According to Table 2D.1, for junior ranks (Ser (a)), the occupancy is 4 personnel.

*1.61s, $0.003378, 976→30 tokens*

#### Claude Opus 4.1

According to Table 2D.1, the occupancy for junior ranks is 4 personnel.

Source: Section 2D3, Table 2D.1 – Planning guidelines for the provision of new domestic facilities

*2.50s, $0.018390, 976→50 tokens*

#### GPT-5

**2D3. Efficiency of occupation.** Allowance may be made for single occupancy for senior officers/VIPs and inefficiencies due to gender segregation. However, an over-generous allocation is not minimum military requirement. Table 2D.1 gives the planning guidance for the provision of new domestic facilities.

| Ser | Personnel | Occupancy |
|-----|-----------|-----------|
| (a) | Junior ranks | 4 personnel |
| (b) | Senior ranks | 4-2 personnel |
| (c) | Junior officers | 4-2 personnel |
| (d) | Senior officers | 1-2 personnel |
| (e) | Command appointments | Single rooms |

**Table 2D.1 – Planning guidelines for the provision of new domestic facilities**

*15.95s, $0.015574, 867→1449 tokens*

---

### Query 2: What are Key User Requirements (KURs) and how do they differ from other priorities?

#### Gemini 2.5 Flash

Key User Requirements (KURs) are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).  Any other priority is coded P1, P2 (and so on) to reflect lower priorities. (Source: data/chapter2.md, section a)


*1.08s, $0.000453, 751→91 tokens*

#### Deepseek

a. **Priority.** A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.

*8.35s, $0.000579, 740→98 tokens*

#### GPT-5 Nano

a. **Priority.** A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.

*8.60s, $0.000669, 747→1580 tokens*

#### Claude Haiku 3.5

According to section 2.a of the context, Key User Requirements (KURs) are defined as:

"Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs)."

In contrast, other priorities are coded as P1, P2, and so on to reflect lower priorities. KURs are considered the most critical requirements that are essential for the facility or service to be functional, while other priorities are ranked in descending order of importance.

*2.65s, $0.001244, 825→146 tokens*

#### GPT-O3

a. **Priority.** A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.

*9.98s, $0.001887, 747→757 tokens*

#### Gemini 2.5 Pro

A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.


*2.16s, $0.002596, 751→95 tokens*

#### Claude Sonnet 4

From the context, here is the relevant passage verbatim:

"Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
- Any other priority is coded P1, P2 (and so on) to reflect lower priorities."

*2.00s, $0.004005, 825→102 tokens*

#### Claude Opus 4.1

Based on the context provided:

**Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).**

**Any other priority is coded P1, P2 (and so on) to reflect lower priorities.**

Source: data/chapter2.md, Section a. **Priority**

*3.48s, $0.020775, 825→112 tokens*

#### GPT-5

a. **Priority.** A priority should be assigned to each element of requirement.¹³
   - Key User Requirements (KURs), are the Critical Success Factors without which the facility/service will not possibly be fit for purpose i.e. not be 'good enough'. During the construction or delivery of support, these may form the basis of Key Performance Indicators (KPIs).
   - Any other priority is coded P1, P2 (and so on) to reflect lower priorities.

*16.85s, $0.011614, 747→1068 tokens*

---

### Query 3: What should the Theatre Infrastructure Development Directive (TIDD) address regarding infrastructure support?

#### Gemini 2.5 Flash

The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'. (2C2.a)


*2.12s, $0.000412, 822→66 tokens*

#### Deepseek

The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'. (Source: data/chapter2.md, 2C2a)

*7.31s, $0.000574, 815→70 tokens*

#### GPT-5 Nano

a. **Infrastructure support to the operation.** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'.

*9.42s, $0.000761, 813→1801 tokens*

#### Claude Haiku 3.5

According to section 2C2(a), the TIDD should explain what infrastructure is required to support the operation. Specific examples provided include:
- 'RSOI camp for 5,000'
- 'APOD for Sp Ac and 24 Typhoon aircraft'
- 'up to 20 company-sized patrol bases'

*1.89s, $0.001053, 896→84 tokens*

#### GPT-O3

a. **Infrastructure support to the operation.** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'.

*7.15s, $0.001208, 813→401 tokens*

#### Gemini 2.5 Pro

The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'. (2C2.a)


*2.63s, $0.002366, 822→66 tokens*

#### Claude Sonnet 4

From section 2C2.a:

"Infrastructure support to the operation. The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'."

*1.89s, $0.003978, 896→86 tokens*

#### Claude Opus 4.1

According to the document, the Theatre Infrastructure Development Directive (TIDD) should address infrastructure support to the operation by explaining what infrastructure is required to support the operation. Examples given include:
- An 'RSOI camp for 5,000'
- An 'APOD for Sp Ac and 24 Typhoon aircraft'
- 'Up to 20 company-sized patrol bases'

Source: Section 2C2.a

*3.44s, $0.021165, 896→103 tokens*

#### GPT-5

**2C2. Contents of a Theatre Infrastructure Development Directive.** The size and contents of the TIDD will vary over time. As a guide it should address:

a. **Infrastructure support to the operation.** The TIDD should explain what infrastructure is required to support the operation, for example, an 'RSOI camp for 5,000', an 'APOD for Sp Ac and 24 Typhoon aircraft', or 'up to 20 company-sized patrol bases'.

*45.52s, $0.020636, 813→1962 tokens*

---

### Query 4: What is an Infrastructure Development Plan and what key elements should it include?

#### Gemini 2.5 Flash

**2C6. Contents of an Infrastructure Development Plan.** Any appropriate format may be used, however, the Infrastructure Development Plan should contain:

a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost. (2C6)

a. **Plan the detailed development of the operational estate.**
   1. Produce infrastructure development plans that are in-tune with the operational plan and Theatre Infrastructure Development Directive. (2D)


*2.70s, $0.000914, 813→268 tokens*

#### Deepseek

An Infrastructure Development Plan should contain:

a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost.

Source: data/chapter2.md, section 2C6 and 2C6.d

*14.61s, $0.000810, 793→218 tokens*

#### GPT-5 Nano

2C6. Contents of an Infrastructure Development Plan. Any appropriate format may be used, however, the Infrastructure Development Plan should contain:

a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost.

*21.78s, $0.001669, 809→4072 tokens*

#### Claude Haiku 3.5

Based on the context provided, an Infrastructure Development Plan is a document that outlines the development and management of a site's infrastructure. According to section 2C6, it should contain the following key elements:

a. **Description of the estate** (2C6a): A brief outline of the site's role, function, and components of the UK's operational estate.

b. **Ownership** (2C6b): Clearly state the boundaries of UK responsibility, clarify land ownership, and establish who is responsible for infrastructure provision, operation, maintenance, and repair.

c. **Planning horizon** (2C6c): Provide a working assumption of the site's likely tenure, derived from the TIDD and adjusted by local plans.

d. **Planned development work** (2C6d): Show site development plans over time, including:
- Site plans illustrating planned development
- A list of major projects
- Estimated time and cost for these projects

Additionally, section 2C7 notes that Infrastructure Development Plans should:
- Be kept under constant review
- Be re-issued periodically
- Be endorsed by PJHQ
- Help shape the next Theatre Infrastructure Development Directive (TIDD)

*4.47s, $0.001757, 866→266 tokens*

#### GPT-O3

**2C6. Contents of an Infrastructure Development Plan.** Any appropriate format may be used, however, the Infrastructure Development Plan should contain:

a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost.

*21.45s, $0.003318, 809→1457 tokens*

#### Gemini 2.5 Pro

2C6. Contents of an Infrastructure Development Plan. Any appropriate format may be used, however, the Infrastructure Development Plan should contain:

a. Description of the estate. An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. Ownership. It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. Planning horizon. Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. Planned development work. The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost.


*2.82s, $0.004249, 813→218 tokens*

#### Claude Sonnet 4

From section 2C6, an Infrastructure Development Plan should contain these key elements:

"a. **Description of the estate.** An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate.

b. **Ownership.** It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair.

c. **Planning horizon.** Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans.

d. **Planned development work.** The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost."

Additionally, from section 2C7:

"As with the TIDD, Infrastructure Development Plans should be kept under constant review and be re-issued on a periodic basis. Infrastructure Development Plans should be endorsed by PJHQ. Each iteration helps shape the next TIDD."

*3.84s, $0.006858, 866→284 tokens*

#### Claude Opus 4.1

Based on the context provided, an Infrastructure Development Plan is a planning document that details the development of operational estate infrastructure. 

According to **Section 2C6**, the Infrastructure Development Plan should contain the following key elements:

a. **Description of the estate** - "An Infrastructure Development Plan should start with a brief outline of the role and function of the site and a list of the components of the UK's operational estate."

b. **Ownership** - "It is important to state clearly the boundaries of UK responsibility (delineate the operational estate). Therefore an Infrastructure Development Plan should clarify ownership of the land and each infrastructure element of the estate. It should establish who is responsible for its provision, operation, maintenance and repair."

c. **Planning horizon** - "Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans."

d. **Planned development work** - "The Infrastructure Development Plan should show, normally in the form of a small number of site plans, how the site is planned to develop over time. This pictorial representation of planned development should be supported by a list of the major projects planned, giving an estimate of time and cost."

According to **Section 2C7**, "Infrastructure Development Plans should be kept under constant review and be re-issued on a periodic basis. Infrastructure Development Plans should be endorsed by PJHQ.

*[Response truncated]*

*6.61s, $0.036015, 866→307 tokens*

#### GPT-5

**Error:** HTTPSConnectionPool(host='api.openai.com', port=443): Read timed out. (read timeout=60)

---

### Query 5: What approvals might be required before occupation of a military facility?

#### Gemini 2.5 Flash

I don't know.  The provided text discusses the planning and management of military infrastructure, including occupancy guidelines (2D3, Table 2D.1), but does not specify any approval processes required before occupation.


*0.97s, $0.000406, 971→46 tokens*

#### Deepseek

I don't know.

*3.57s, $0.000543, 955→5 tokens*

#### GPT-5 Nano

b. **Military works area.** A military works area defines the geographic boundaries within which the needs of operational imperatives may be balanced against other regulatory obligations, for example, operational risk may be taken. The boundary of a military works area will usually be coincident with the joint operations area (JOA). Only PJHQ can establish and disestablish a military works area.³ During the life of a military works area there is likely to be a migration from a policy of hastily provided operationally essential infrastructure having a short life and probably incorporating a degree of risk, towards longer lasting infrastructure which is more compliant with UK Health and Safety standards and other statutory obligations. The path and pace of this migration must remain the responsibility of the operational commander, advised by his Infrastructure Staff. Migration may not be homogenous across all areas of a military works area; the commander and his Infrastructure Staff will need to be very clear about what risks can be taken in each part of the military works area.

*13.20s, $0.000950, 966→2255 tokens*

#### Claude Haiku 3.5

Based on the provided context, I cannot find a direct answer about specific approvals required before occupation of a military facility. The context discusses infrastructure planning guidelines, occupancy rates, and military works areas, but does not explicitly outline pre-occupation approval processes. To provide a definitive answer about required approvals, I would need additional documentation.

The closest relevant information is in section 204, which suggests that military commanders are responsible for determining infrastructure policy and risk assessments, and in section 2D4, which indicates that any variations from standard guidelines must be explicitly stated in the Tactical Infrastructure Recce Report. However, this does not constitute a comprehensive approval process.

*3.50s, $0.001386, 1038→139 tokens*

#### GPT-O3

I don't know

*6.72s, $0.001037, 966→277 tokens*

#### Gemini 2.5 Pro

I don't know.


*1.95s, $0.001908, 971→7 tokens*

#### Claude Sonnet 4

From the provided context, I cannot find a specific passage that directly addresses what approvals are required before occupying a military facility. While the text discusses Military Works Areas, infrastructure management, and reconnaissance requirements, it does not explicitly state the approval process for facility occupation.

*2.07s, $0.003954, 1038→56 tokens*

#### Claude Opus 4.1

I don't know. The provided context does not contain information about what approvals might be required before occupation of a military facility. The context discusses planning guidelines for domestic facilities, risk management in military works areas, and information needs for reconnaissance, but does not specify approval requirements for facility occupation.

*3.24s, $0.020145, 1038→61 tokens*

#### GPT-5

**Error:** HTTPSConnectionPool(host='api.openai.com', port=443): Read timed out. (read timeout=60)

---

### Query 6: What is the purpose and content of a Statement of Need (SON) in infrastructure planning?

#### Gemini 2.5 Flash

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it

*[Response truncated]*

*2.49s, $0.000984, 864→290 tokens*

#### Deepseek

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it

*[Response truncated]*

*17.43s, $0.000963, 849→290 tokens*

#### GPT-5 Nano

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it

*[Response truncated]*

*12.57s, $0.001008, 864→2412 tokens*

#### Claude Haiku 3.5

Based on paragraph 242, the Statement of Need (SON) serves the following purposes:

1. To clarify the requirement for infrastructure support
2. Is raised by the unit or organization requiring new infrastructure (the user or sponsor)
3. Helps identify what is actually needed, not just what is wanted
4. Can be expanded into a more detailed User Requirement Document (URD)
5. Provides a basis for documenting and assessing infrastructure requirements

The document specifically notes that the Statement of Need is "in common use" in military organizations, and is typically used to capture the initial infrastructure requirement. An example format for creating a Statement of Need is referenced in Annex 2A of the document.

The paragraph emphasizes the importance of focusing on identifying the actual need, stating: "it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project."

*4.30s, $0.001519, 914→197 tokens*

#### GPT-O3

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it

*[Response truncated]*

*12.74s, $0.003354, 864→1461 tokens*

#### Gemini 2.5 Pro

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it

*[Response truncated]*

*3.74s, $0.005245, 864→290 tokens*

#### Claude Sonnet 4

**242.** **Statement of Need and User Requirement Document.** The requirement for any infrastructure support should be clarified through a Statement of Need (SON)/Statement of Need (SOR). The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need/Statement of Need. Most military organisations are familiar with describing this as a 'requirement' and so the term Statement of Need is in common use. However, as explained earlier, it is important to identify what is actually needed and so the term Statement of Need is often used when managing the subsequent project. The usual practice is to expand on the Statement of Need/Statement of Need to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). Annex 2A shows an example of the format a unit may use to make its Statement of Need. Where appropriate the Statement of Need can be followed up with a User Requirement Document. The User Requirement Document provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the User Requirement Document a serial number should be assigned to each element of requirement. It should describe the requirement in output terms and articulate the standard required. The requirement should state what effect is required. It should say how the infrastructure will be used, allowing the designers to determine the best way to achieve it

*[Response truncated]*

*4.95s, $0.007137, 914→293 tokens*

#### Claude Opus 4.1

Based on the context provided:

The Statement of Need (SON) serves to clarify the requirement for any infrastructure support. The unit or organisation requiring the new infrastructure (the user or sponsor) is responsible for raising the Statement of Need. The purpose is to identify what is actually needed rather than what is wanted.

The Statement of Need can be expanded upon to identify and capture the elements of the requirement in a tabulated User Requirement Document (URD). The URD provides a written record that can be used to assess whether what is delivered matches what was originally requested. In the URD, each element of requirement should be assigned a serial number, describe the requirement in output terms, articulate the standard required, and state what effect is required. It should explain how the infrastructure will be used, allowing designers to determine the best way to achieve it.

Source: Section 242 - Statement of Need and User Requirement Document

*4.79s, $0.028185, 914→193 tokens*

#### GPT-5

**Error:** API error: 404 - {
    "error": {
        "message": "Your organization must be verified to use the model `gpt-5`. Please go to: https://platform.openai.com/settings/organization/general and click on Verify Organization. If you just verified, it can take up to 15 minutes for access to propagate.",
        "type": "invalid_request_error",
        "param": null,
        "code": "model_not_found"
    }
}


---

### Query 7: How should surge capacity be considered when sizing military bases?

#### Gemini 2.5 Flash

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time. (Source: data/chapter2.md)


*0.88s, $0.000458, 1017→61 tokens*

#### Deepseek

The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time. (Source: data/chapter2.md, section c)

*5.92s, $0.000632, 969→53 tokens*

#### GPT-5 Nano

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

*7.36s, $0.000635, 973→1467 tokens*

#### Claude Haiku 3.5

According to section c under the context, bases should be capable of accommodating 125% of their design capacity for a limited period of time to allow for surges during emergencies or rotations. Specifically, the text states: "As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time."

*2.04s, $0.001174, 1082→77 tokens*

#### GPT-O3

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

*10.13s, $0.001391, 973→452 tokens*

#### Gemini 2.5 Pro

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time. (data/chapter2.md)


*2.76s, $0.002644, 1017→59 tokens*

#### Claude Sonnet 4

"Allow for surges. The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time."

*1.53s, $0.004026, 1082→52 tokens*

#### Claude Opus 4.1

Based on the context provided:

**Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

Source: Section 246.c from data/chapter2.md

*3.33s, $0.021855, 1082→75 tokens*

#### GPT-5

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

*9.20s, $0.008206, 973→699 tokens*

---

### Query 8: What guidance should a TIDD provide about the planning horizon for infrastructure investments?

#### Gemini 2.5 Flash

The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)? (2C2.b)


*0.92s, $0.000418, 836→67 tokens*

#### Deepseek

**2C2. Contents of a Theatre Infrastructure Development Directive.** The size and contents of the TIDD will vary over time. As a guide it should address:

b. **Planning horizon.** The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*9.06s, $0.000634, 833→100 tokens*

#### GPT-5 Nano

The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*9.69s, $0.000709, 832→1668 tokens*

#### Claude Haiku 3.5

According to section 2C2(b), the TIDD should:

"give the planning horizon for infrastructure investements throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?"

Additionally, section 2C(c) reinforces this by stating the need to "Give the working assumption of the likely tenure of the site, derived from the TIDD and adjusted by local plans."

*2.31s, $0.001214, 903→123 tokens*

#### GPT-O3

b. **Planning horizon.** The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*11.62s, $0.002376, 832→980 tokens*

#### Gemini 2.5 Pro

The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)? (2C2. b)


*1.73s, $0.002405, 836→67 tokens*

#### Claude Sonnet 4

b. **Planning horizon.** The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*1.69s, $0.003789, 903→72 tokens*

#### Claude Opus 4.1

Based on the context provided:

The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

Source: Section 2C2.b

*3.21s, $0.019695, 903→82 tokens*

#### GPT-5

b. **Planning horizon.** The TIDD should give the planning horizon for infrastructure investments throughout theatre. Ideally, some estimate should be given of the likely tenure of each site and major facility; are they likely to be needed for a short term (less than say six months) or longer term (say up to two years)?

*18.98s, $0.012030, 832→1099 tokens*

---

### Query 9: What is a Variation Order (VO) and when is it typically used in military infrastructure projects?

#### Gemini 2.5 Flash

248. Changing the Requirement. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.


*0.92s, $0.000426, 853→68 tokens*

#### Deepseek

**248.** **Changing the Requirement.** Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*15.15s, $0.000832, 832→218 tokens*

#### GPT-5 Nano

If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*5.92s, $0.000479, 844→1092 tokens*

#### Claude Haiku 3.5

Based on section 248 of the document, a Variation Order (VO) is used when there is a need to change a project requirement midway through construction. Specifically, the document states that when it becomes clear that the original requirement is incomplete or has changed, a project engineer will obtain the cost of the change and note it on a Variation Order. 

The key points about a Variation Order are:
1. It documents changes to the original project requirement
2. The project engineer calculates the cost of the change
3. Work on a Variation Order should not begin without confirming adequate financing
4. A record must be kept explaining the reasons for the requirement change

The document also cautions that most project delays stem from user-initiated changes during construction and a lack of change control, so such variations should be carefully considered.

*4.01s, $0.001450, 918→179 tokens*

#### GPT-O3

**248.** **Changing the Requirement.** Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*9.36s, $0.002052, 844→815 tokens*

#### Gemini 2.5 Pro

Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement. (248)


*3.06s, $0.004349, 853→220 tokens*

#### Claude Sonnet 4

**248.** **Changing the Requirement.** Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*4.77s, $0.006354, 918→240 tokens*

#### Claude Opus 4.1

Based on the context provided, a Variation Order (VO) is a document used when there is a change to the original requirement during a military infrastructure project. 

According to Section 248 "Changing the Requirement," when a change to the project requirement is needed, "the project engineer will obtain the cost and note it on a Variation Order (VO)." The section further states that "Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs."

A VO is typically used when it becomes clear that the original requirement was incomplete or has changed since project inception, making the facility potentially unfit-for-purpose once completed. It documents the cost implications of the change and ensures proper financial authorization before proceeding with any variation work.

*5.54s, $0.026445, 918→169 tokens*

#### GPT-5

**248.** **Changing the Requirement.** Occasionally it may be become clear that the requirement was incomplete or has changed since project inception such that the facility will not be fit-for-purpose once completed. A judgement must then be made as to whether to change the requirement and alter the build in progress, or wait until project completion to make adjustments. Often the latter is better as it delivers the facility with the earliest possible initial operating capability, avoids contract disputes and keeps costs down. Most project delays can be attributed to user-instigated changes midway through construction and a lack of change control by the infrastructure staff. A value judgement must be made after seeking engineer advice. It is important that all parties must recognise that decisions made by the user that agreed the requirement at the start of a project, are binding on successors. If a change is required, the project engineer will obtain the cost and note it on a Variation Order (VO). Work on a Variation Order should not be undertaken without checking that there is adequate finance to cover any additional costs. A record must be kept of the reasons for any change in requirement.

*35.56s, $0.015515, 844→1446 tokens*

---

### Query 10: What factors should be considered when planning for base population and contractor presence?

#### Gemini 2.5 Flash

b. **Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel. (Source: data/chapter2.md, section b)

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time. (Source: data/chapter2.md, section c)


*1.39s, $0.000649, 905→151 tokens*

#### Deepseek

b. **Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

a. **Plan for the base's capability.** By not considering the military capability required at a base, planners will usually under-estimate a Force's reliance on infrastructure. For example, they may assume that weapons and ammunition will be permanently held on vehicles or by personnel, however, a few months into the deployment, the requirement for a magazine and armoury will become apparent. Other facilities typically over-looked are: kitchen and refrigerated food storage, vehicle repair facilities, ranges, parking, entry control point facilities and communications masts. Similarly, planners will often give an arbitrary size of a camp or base determined largely on strategic considerations rather than a manpower estimate against task lines, for example, 'we need a 100-man base at this location'. This invariably leads to an under-estimate in base size.

*17.85s, $0.000961, 867→283 tokens*

#### GPT-5 Nano

b. **Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.

| Ser | Military | Contractors | Ratio | Remarks |
|-----|----------|-------------|--------|---------|
| (a) | 4,200 | 2,400 | 1:1.75 | 530 UK-based contractors, 110 Third Country nationals, 790 Locally recruited workers |
| (b) | 8,000 | 3,200 | 1:2.5 | |

**Table 2.1 – Contractors as a proportion of the force**

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

---
**246.** **Avoid under-estimating the requirement.** Avoid under-estimating the requirement as changes are difficult to accommodate.

a. **Plan for the base's capability.** By not considering the military capability required at a base, planners will usually under-estimate a Force's reliance on infrastructure. For example, they may assume that weapons and ammunition will be permanently held on vehicles or by personnel, however, a few months into the deployment, the requirement for a magazine and armoury will become apparent. Other facilit

*[Response truncated]*

*25.13s, $0.001956, 883→4779 tokens*

#### Claude Haiku 3.5

Based on the context, here are the key factors to consider when planning for base population and contractor presence:

1. Total Population Consideration (Section b):
"Military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked." The context provides a table (Table 2.1) showing the ratio of military personnel to contractors, which ranges from 1:1.75 to 1:2.5, including:
- UK-based contractors
- Third Country nationals
- Locally recruited workers

2. Surge Capacity (Section c):
"Bases should be capable of accommodating 125% of the design capacity for a limited period of time" to allow for emergencies or rotation.

3. Avoid Underestimating Requirements (Section 246a):
Planners should consider:
- Military capability requirements
- Infrastructure needs beyond personnel numbers
- Facilities like:
  * Magazines and armories
  * Kitchen and food storage
  * Vehicle repair facilities
  * Ranges
  * Parking
  * Entry control points
  * Communication masts

4. Experience-Based Planning (Section 228):
Rely on personnel who have recent experience building similar infrastructure in similar locations.

*5.22s, $0.001854, 962→271 tokens*

#### GPT-O3

• Count everyone, not just soldiers – include civilian contractors plus any MOD or other-government-department personnel (data/chapter2.md, b. “Consider the total population”).  

• Use recent operational ratios as a guide (e.g., 4 200 military : 2 400 contractors or 8 000 : 3 200) to size facilities for contractor presence (Table 2.1, data/chapter2.md).  

• Design the base to handle short-term surges of up to 125 % of its nominal capacity for emergencies or rotations (data/chapter2.md, c. “Allow for surges”).  

• Avoid under-estimating needs: plan for all supporting infrastructure (magazines, kitchens, workshops, parking, entry control points, comms masts, etc.) instead of fixing an arbitrary camp size (data/chapter2.md, §246 a. “Plan for the base's capability”).

*10.83s, $0.001646, 883→602 tokens*

#### Gemini 2.5 Pro

Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.


*1.55s, $0.002522, 905→66 tokens*

#### Claude Sonnet 4

b. **Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.

c. **Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

*2.97s, $0.004881, 962→133 tokens*

#### Claude Opus 4.1

Based on the context provided, the following factors should be considered when planning for base population and contractor presence:

**Consider the total population.** Furthermore, military planning is usually based on numbers of military personnel, and unfortunately civilians are often over-looked. Table 2.1 shows the relative numbers of civilian contractors that will work alongside a Force and is based on recent operational experience. To this should be added any MOD or Other Government Department (OGD) personnel.

**Allow for surges.** The final calculation of size must allow for surge either during emergencies or during rotation. As a practical guide, bases should be capable of accommodating 125% of the design capacity for a limited period of time.

**Plan for the base's capability.** By not considering the military capability required at a base, planners will usually under-estimate a Force's reliance on infrastructure. For example, they may assume that weapons and ammunition will be permanently held on vehicles or by personnel, however, a few months into the deployment, the requirement for a magazine and armoury will become apparent. Other facilities typically over-looked are: kitchen and refrigerated food storage, vehicle repair facilities, ranges, parking, entry control point facilities and communications masts. Similarly, planners will often give an arbitrary size of a camp or base determined largely on strategic considerations rather than a manpower estimate against

*[Response truncated]*

*6.97s, $0.040155, 962→343 tokens*

#### GPT-5

**Error:** HTTPSConnectionPool(host='api.openai.com', port=443): Read timed out. (read timeout=60)

---

## Cost Analysis

- **Most Expensive:** 0.252825 USD
- **Least Expensive:** 0.005431 USD
- **Average Cost:** 0.052485 USD

## Performance Analysis

- **Fastest Average Response:** 1.42 seconds
- **Slowest Average Response:** 23.68 seconds
- **Average Response Time:** 8.10 seconds

## Enhanced Recommendations (Quality + Performance)

### Best Overall Model: Claude Haiku 3.5
- **Quality Score:** 0.83 (highest overall evaluation)
- **Speed:** 3.15s (3rd fastest)
- **Cost:** $0.013560 (2nd most cost-effective)
- **Strengths:** Excellent section citations (0.90), strong citation coverage (0.90)
- **Use Case:** Primary choice for production RAG where accuracy is critical

### Best Budget Choice: Deepseek
- **Quality Score:** 0.80 (tied for 2nd)
- **Speed:** 11.04s (moderate)  
- **Cost:** $0.007277 (most cost-effective)
- **Strengths:** Excellent verbatim quoting (0.90), strong citation coverage (0.90)
- **Use Case:** Cost-sensitive applications where quality remains important

### Best Speed/Quality Balance: Gemini 2.5 Flash
- **Quality Score:** 0.77 (5th place)
- **Speed:** 1.42s (fastest)
- **Cost:** $0.005431 (2nd most cost-effective)
- **Strengths:** Fast responses, good citation coverage (0.90)
- **Use Case:** Real-time applications where speed is critical

### Premium Choice: Claude Sonnet 4
- **Quality Score:** 0.80 (tied for 2nd)
- **Speed:** 2.73s (2nd fastest)
- **Cost:** $0.048360 (expensive but justified)
- **Strengths:** Excellent verbatim quoting (0.90), fast responses
- **Use Case:** High-value applications where both speed and quality matter

### Key Insights from LLM Judge Evaluation

1. **Quality varies significantly**: Scores range from 0.43 (GPT-5) to 0.83 (Claude Haiku 3.5)
2. **Section citation is challenging**: Only Claude models consistently cite section numbers properly
3. **Cost doesn't predict quality**: Deepseek (cheapest) outperforms many expensive models
4. **Speed vs Quality tradeoff**: Fastest model (Gemini Flash) achieves good but not top quality

## Technical Notes

- All models were tested with the same RAG context (k=4 documents)
- Temperature was set to 0.0 for consistent responses
- Maximum tokens per response: 1000
- Timeout: 60 seconds per request
- Rate limiting: 0.5s delay between requests

*Report generated by model_comparison.py on 2025-09-03 10:54:37*
