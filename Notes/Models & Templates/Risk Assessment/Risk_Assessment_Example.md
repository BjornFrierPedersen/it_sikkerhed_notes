# Risk Assessment Example

This document provides an example of a risk assessment table based on the methodology described in the Risk Assessment Guidance document.

## Complete Risk Assessment Table

### Risk Assessment Section

| Risk - What might affect confidentiality, availability or integrity | Risk owner | Why is this a threat/risk? | Estimate Consequence | Estimate Probability | Why is the probability of this assessed? | Calculated risk | Accepted |
|------------------------------------------------------------------|------------|---------------------------|---------------------|---------------------|------------------------------------------|----------------|----------|
| Breaching confidentiality of customer data by disclosing it to the person concerned | Head of administration | Accidental disclosure of confidential customer data to competitors can mean loss of customers and/or breaches of personal data security can mean loss of reputation and sanctions/fines. | 4 | 2 | Collections of customer data reside in only two systems, both of which have limited access and which are protected by the Ajax firewall and security systems. The employees receive instruction in correct use. The customer data are backed up so that it can be quickly re-established on another server and the IT systems are operated by experienced employees. | 8 | Yes |
| Outage of the availability of IT system going down. Breach of the integrity of the products by corrupting data used in the production process. | IT manager | If production data is not reliable when it needs to be used, it can affect the products and delivery. | 3 | 1 | | 3 | Yes |
| | Operations manager | Even minor errors in critical parameters and results in a database that can affect the customer's health. | 4 | 4 | | 16 | Avoid |

### Risk Management Section

| Why is the probability of this assessed? | Calculated risk | Accepted | New measures | Consequences after new measures | New probability | New residual risk | Accepted | Conclusion | Willingness to take risk | Explanation |
|------------------------------------------|----------------|----------|--------------|--------------------------------|----------------|-------------------|----------|------------|-------------------------|-------------|
| Collections of customer data reside in only two systems, both of which have limited access and which are protected by the Ajax firewall and security systems. The employees receive instruction in correct use. The customer data are backed up so that it can be quickly re-established on another server and the IT systems are operated by experienced employees. | 8 | Yes | | | | 0 | | It will be prohibitively expensive to do more, so residual risks are accepted. | Green | Management's assessment of the lowest risk score, which is GREEN |
| | 3 | Yes | | | | 0 | | | 1 | Management's assessment of the lowest risk score, which is GREEN |
| The production network has been connected to the rest of the network, but no new measures have been implemented. | 16 | Avoid | The measures from the rest of the network must be implemented in the production network | 4 | 2 | 8 | | There are older systems on the production network. When they are upgraded naturally the probability will decrease | Yellow | Management's assessment of the lowest risk score, which is YELLOW |
| | 0 | | | | | 0 | | | 6 | Management's assessment of the lowest risk score, which is YELLOW |
| | 0 | | | | | 0 | | | Red | Management's assessment of the lowest risk score, which is RED |
| | 0 | | | | | 0 | | | 10 | Management's assessment of the lowest risk score, which is RED |

### Risk Details

| Risk - What might affect confidentiality, availability or integrity | Risk owner | Why is this a threat/risk? | Impact Description |
|------------------------------------------------------------------|------------|---------------------------|-------------------|
| Breaching confidentiality of customer data by disclosing it to the person concerned | Head of administration | Accidental disclosure of confidential customer data to competitors can mean loss of customers and/or breaches of personal data security can mean loss of reputation and sanctions/fines. | Loss of major customers or many customers will be serious. And today the fines can be high. |
| Outage of the availability of IT system going down. Breach of the integrity of the products by corrupting data used in the production process. | IT manager | If production data is not reliable when it needs to be used, it can affect the products and delivery. | Delays in delivery or delivery failures that could lead to a loss of dissatisfied customers. Stories that products have harmed consumers can, in addition to direct compensation, significantly affect sales and reputation. |

## Risk Classification

The risk scores are calculated by multiplying the consequence score (1-5) by the probability score (1-5), resulting in a risk score between 1-25. These scores are categorized as follows:

* **Green**: Low risk (5 or below) - risks can be immediately accepted
* **Yellow**: Medium risk (6 to 9) - periodic review required
* **Red**: High risk (10 or more) - action should be taken to manage the risk

### Consequence Scale
1. Very small consequence – it is really of no significance
2. Small consequence – it can be handled as part of the operation
3. Some consequence – extra resources will probably have to be found
4. High consequence – it has an impact on the bottom line
5. Very large consequence – the company is threatened

### Probability Scale
1. Rare or unlikely
2. Will hardly occur
3. Is possible
4. Must be expected to happen
5. Will be exploited

## Using This Example

This example demonstrates a complete risk assessment process:

1. **Risk Identification**: Specify what might affect confidentiality, availability, or integrity
2. **Risk Ownership**: Assign each risk to an appropriate owner in the organization
3. **Threat/Risk Description**: Explain why this is a concern
4. **Impact Assessment**: Determine severity of consequences (1-5 scale)
5. **Probability Assessment**: Determine likelihood of occurrence (1-5 scale)
6. **Risk Calculation**: Multiply consequence by probability
7. **Risk Acceptance**: Determine if the risk is acceptable or requires mitigation
8. **Mitigation Planning**: Define new measures for unacceptable risks
9. **Residual Risk Assessment**: Recalculate risk after mitigation measures
10. **Conclusion and Follow-up**: Document decisions and next steps

This format can be used as a template for creating your own comprehensive risk assessment based on the identified risks in your organization. 