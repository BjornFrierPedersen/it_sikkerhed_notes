# [[_content/dictionary#O|OWASP]] Application Security Verification Standard ([[_content/dictionary#A|ASVS]]) 4.0.3

## Om standarden
- **Formål**: [[_content/dictionary#A|ASVS]] er en omfattende liste over sikkerhedskrav og tests, der hjælper med at definere, bygge, teste og verificere sikre applikationer.
- **Version**: 4.0.3, udgivet i oktober 2021.
- **Licens**: Creative Commons Attribution ShareAlike 3.0.

## Nye funktioner i 4.0
- **[[_content/dictionary#N|NIST]] 800-63-3**: Introduktion af moderne, evidensbaserede autentificeringskontroller.
- **Renummerering**: Hele [[_content/dictionary#A|ASVS]] er renummereret for at lukke huller og segmentere længere kapitler.
- **[[_content/dictionary#C|CWE]]-mapping**: Omfattende mapping til Common Weakness Enumeration ([[_content/dictionary#C|CWE]]).
- **Mobilkapitel pensioneret**: Flyttet til Mobile Application Security Verification Standard ([[_content/dictionary#M|MASVS]]).

## Anvendelse af [[_content/dictionary#A|ASVS]]
- **Sikkerhedsniveauer**: Tre niveauer (Level 1, 2 og 3) med stigende dybde.
  - **Level 1**: Lavt sikkerhedsniveau, fuldt penetrationstestbart.
  - **Level 2**: Anbefalet niveau for de fleste applikationer med følsomme data.
  - **Level 3**: Højeste sikkerhedsniveau for kritiske applikationer.

## Vigtige kapitler og krav

### V1-V5: Grundlæggende sikkerhed
- **V1 Arkitektur, Design og Trusselsmodellering**: Fokus på sikker softwareudviklingslivscyklus, autentificeringsarkitektur, sessionsstyring, adgangskontrol og kryptografisk arkitektur.
- **V2 Autentificering**: Krav til password-sikkerhed, generel autentificeringssikkerhed, autentificeringslivscyklus og credential storage.
- **V3 Sessionsstyring**: Grundlæggende sikkerhed, sessionsbinding, sessionsterminering og cookie-baseret sessionsstyring.
- **V4 Adgangskontrol**: Generel design, operationel adgangskontrol og andre overvejelser.
- **V5 Validering, Sanitering og Kodning**: Inputvalidering, sanitering og sandboxing, outputkodning og injektionsforebyggelse.

### V6-V10: Data og systembeskyttelse
- **V6 Lagring af Kryptografi**: Dataklassificering, algoritmer, tilfældige værdier og hemmelighedsstyring.
- **V7 Fejlhåndtering og Logning**: Logindhold, logbehandling, logbeskyttelse og fejlhåndtering.
- **V8 Databeskyttelse**: Generel databeskyttelse, klient-side databeskyttelse og følsomme private data.
- **V9 Kommunikation**: Klient- og serverkommunikationssikkerhed.
- **V10 Ondsindet kode**: Kodeintegritet, søgning efter ondsindet kode og applikationsintegritet.

### V11-V14: Specifikke funktionsområder
- **V11 Forretningslogik**: Sikkerhed i forretningslogik, herunder sekventiel behandling og anti-automatiseringskontroller.
- **V12 Filer og Ressourcer**: Filupload, filintegritet, filudførelse, filopbevaring og filnedlasting.
- **V13 [[_content/dictionary#A|API]] og Webservice**: Generel webservice-sikkerhed, [[_content/dictionary#R|REST]]ful webservice, [[_content/dictionary#S|SOAP]] webservice og GraphQL.
- **V14 Konfiguration**: Bygning og udrulning, afhængigheder, utilsigtet sikkerhedsafsløring og [[_content/dictionary#H|HTTP]]-sikkerhedsoverskrifter.

## Appendices
- **Appendix A: Ordliste** - Definitioner af centrale termer og forkortelser som [[_content/dictionary#A|API]], [[_content/dictionary#A|ASVS]], [[_content/dictionary#C|CWE]], [[_content/dictionary#J|JWT]], [[_content/dictionary#N|NIST]], [[_content/dictionary#O|OWASP]] med flere.
- **Appendix B: Referencer** - Liste over nyttige [[_content/dictionary#O|OWASP]]-projekter og eksterne ressourcer der kan være nyttige for brugere af standarden.
- **Appendix C: Internet of Things Verifikationskrav** - Sikkerhedskrav specielt udviklet til [[_content/dictionary#I|IoT]]-enheder i samarbejde med [[_content/dictionary#O|OWASP]] Internet of Things projektledere, med referencer til [[_content/dictionary#O|OWASP]] [[_content/dictionary#I|IoT]] Top 10 2018. 