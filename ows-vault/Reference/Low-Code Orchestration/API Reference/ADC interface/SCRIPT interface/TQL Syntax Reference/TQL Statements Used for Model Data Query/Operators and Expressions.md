---
title: "Operators and Expressions"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/adc_tql_010.html"
depth: 6
---
#### Operands

For TQL statements used for model data query, the operand can be one of the following. The specific operand that can be used depends on its location.

**Table 1** Operands  
| Operand Type | Description |
| :-- | :-- |
| Model property | A model property is presented in the form of identifiers. The model property format should meet the identifier format conditions. For details, see Identifier. In the scenario where multiple models are associated for query and subqueries exist, to prevent ambiguity of multiple properties with the same name in the same context, add a model name (or alias of the model name in the query) in front of the property name and the alias of the subquery to distinguish these properties. |
| Constant | A constant can be a digit, string, or Boolean value. |
| Function | For details, see TQL Functions. |
| Expression | For details, see Expression. |