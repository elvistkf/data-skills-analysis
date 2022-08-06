ner_data = [
    (
        "Bachelor’s degree in Information Technology, Computer Science or related disciplines", 
        [
            (0, 8, "degree"),
            (21, 43, "major"),
            (45, 61, "major")
        ]
    ),
    (
        "Good command of SQL, Excel, VBA, ETL. Knowledge in Python, R, Tableau a plus",
        [
            (16, 19, "programming"),
            (21, 26, "BI"),
            (28, 31, "programming"),
            (51, 57, "programming"),
            (59, 60, "programming"),
            (62, 69, "BI")
        ]
    ),
    (
        "Experience in data analytics technologies, e.g. Redshift, AWS an advantage",
        [
            (48, 56, "cloud"),
            (58, 61, "cloud")
        ]
    ),
    (
        "Well versed in Microsoft Office, a high level of financial/business analysis capacity including use of Excel, Word & Powerpoint",
        [
            (103, 108, "BI")
        ]
    ),
    (
        "Degree or above in IT, CS and Computing Engineering or equivalent",
        [
            (19, 21, "major"),
            (30, 51, "major")
        ]
    ),
    (
        "Experience in SQL and programming skill will be an advantage;",
        [
            (14, 17, "programming")
        ]
    ),
    (
        "Experience in MS Power BI suite",
        [
            (17, 25, "BI")
        ]
    ),
    (
        "High proficient in SQL, data modeling",
        [
            (19, 22, "programming")
        ]
    ),
    (
        "Knowledge of Microsoft Azure / Hotjar / MS Clarity / HTML / Python / R / machine learning is an advantage",
        [
            (23, 28, "cloud"),
            (53, 57, "programming"),
            (60, 66, "programming"),
            (69, 70, "programming")
        ]
    ),
    (
        "Bachelor’s degree in Data Science, Statistics, Mathematics or related quantitative disciplines with 3-year relevant experience",
        [
            (0, 8, "degree"),
            (21, 33, "major"),
            (35, 45, "major"),
            (47, 58, "major")
        ]
    ),
    (
        "Knowledge in Big Data Tools and Architecture (e.g., Hadoop, PySpark)",
        [
        ]
    ),
    (
        "Proficiency in SQL, Python/R/Scala",
        [
            (15, 18, "programming"),
            (20, 26, "programming"),
            (27, 28, "programming"),
            (29, 34, "programming")
        ]
    ),
    (
        "Good command in Unix and Git commands",
        [
        ]
    ),
    (
        "Knowledge of BI/visualization tools (e.g., Tableau, Qlik, SAS) is a plus",
        [
            (43, 50, "BI"),
            (52, 56, "BI"),
            (58, 61, "programming")
        ]
    ),
    (
        "Bachelor degree in Information Technology, Insurance, Business or related disciplines",
        [
            (0, 8, "degree"),
            (19, 41, "major"),
            (54, 62, "major")
        ]
    ),
    (
        "1-2 years of experience in VBA, Tableau, PowerBI, SQL programming is a plus",
        [
            (27, 30, "programming"),
            (32, 39, "BI"),
            (41, 48, "BI"),
            (50, 53, "programming")
        ]
    ),
    (
        "Bachelor’s or Master’s degree majored in Marketing, Information Science, Statistics, etc.",
        [
            (0, 8, "degree"),
            (14, 20, "degree"),
            (41, 50, "major"),
            (52, 71, "major"),
            (73, 83, "major")
        ]
    ),
    (
        "Strong in MS excel, data mining languages like SQL, open-source R or Python, and data visualization using BI tools (Tableau, MicroStrategy, etc)",
        [
            (13, 18, "programming"),
            (47, 50, "programming"),
            (64, 65, "programming"),
            (69, 75, "programming"),
            (116, 123, "BI"),
            (125, 138, "BI")
        ]
    ),
    (
        "Knowledge of project management lifecycle & methodologies (e.g. PMP, SDLC, Agile, etc.) and typical problems associated with the implementation of projects.",
        [
        ]
    ),
    (
        "With strong hands on experience on program coding such as C / C++, COBOL, SQL ",
        [
            (58, 59, "programming"),
            (62, 65, "programming"),
            (67, 72, "programming"),
            (74, 77, "programming")
        ]
    ),
    (
        "Experience in C / C++, COBOL, Oracle, Linux OpenVMS ",
        [
            (14, 15, "programming"),
            (18, 21, "programming"),
            (23, 28, "programming"),
            (30, 36, "DB")
        ]
    ),
    (
        "Finance or accounting background with a strong focus in financial analysis (e.g., through coursework, CFA or equivalent, or relevant work experience).",
        [
            (0, 7, "major")
        ]
    ),
    (
        "Working knowledge of MS Excel, Word and PowerPoint.",
        [
            (24, 29, "BI")
        ]
    ),
    (
        "Bachelor degree in Business, Information Technology, Marketing or relevant disciplines",
        [
            (0, 8, "degree"),
            (19, 27, "major"),
            (29, 51, "major"),
            (53, 62, "major")
        ]
    ),
    (
        "Good knowledge in SQL, PL/SQL and RDBMS",
        [
            (18, 21, "programming"),
            (23, 29, "programming")
        ]
    ),
    (
        "Proficiency in Python or R, and the libraries/packages for quantitative analysis and data mining",
        [
            (15, 21, "programming"),
            (25, 26, "programming")
        ]
    ),
    (
        "Experience with relational databases (MySQL, PostgreSQL) and time series databases (KDB/Q, InfluxDB, DolphinDB);",
        [
            (38, 43, "DB"),
            (45, 55, "DB"),
            (84, 89, "DB"),
            (91, 99, "DB"),
            (101, 110, "DB")
        ]
    ),
    (
        "Experience with AWS and GitLab is a plus; ",
        [
            (16, 19, "cloud"),
        ]
    ),
    (
        "Strong academic background in quantitative subject, e.g. Physics, Mathematics, Computer Science, Statistics, Engineering or related disciplines;",
        [
            (57, 64, "major"),
            (66, 77, "major"),
            (79, 95, "major"),
            (97, 107, "major"),
            (109, 120, "major")
        ]
    ),
    (
        "Advance with technical tools like Alteryx, Power BI, Qlik Sense and Tableau ",
        [
            (34, 41, "BI"),
            (43, 51, "BI"),
            (53, 57, "BI"),
            (68, 75, "BI")
        ]
    ),
    (
        "Experience in IFRS17, LIFE/Asia, Oracle PL/SQL, MS SQL and/or digital applications are strongly preferred.",
        [
            (40, 46, "programming"),
            (48, 54, "programming"),
            (51, 54, "programming")
        ]
    ),
    (
        "Experience in agile methodology, writing business and functional requirements document and driving user stories grooming sessions",
        [
        ]
    ),
    (
        "Experience with all phases of Software Development Life Cycle (SDLC)",
        [
        ]
    ),
    (
        "Degree holder in IT and data sciences related subjects",
        [
            (17, 19, "major"),
            (24, 37, "major")
        ]
    ),
    (
        "Good knowledge of major data programming languages and analytic tools such as Python, Hadoop, Tableau, MS SQL, Oracle RDBMS, PL SQL, Azure Cloud, Microsoft Power BI, Excel Power Query, Google Analytics, Google Data Studio highly preferred",
        [
            (78, 84, "programming"),
            (94, 101, "BI"),
            (103, 109, "programming"),
            (106, 109, "programming"),
            (125, 131, "programming"),
            (111, 123, "DB"),
            (133, 138, "cloud"),
            (156, 164, "BI"),
            (166, 171, "BI"),
            (185, 201, "BI"),
            (203, 221, "BI")
        ]
    ),
    (
        "Proficient in SAS, SQL, Python or other data mining tools",
        [
            (14, 17, "programming"),
            (19, 22, "programming"),
            (24, 30, "programming")
        ]
    ),
    (
        "Practical experience in data visualization tools (e.g. Qlik View/Sense, Power BI or Tableau);",
        [
            (55, 59, "BI"),
            (72, 80, "BI"),
            (84, 91, "BI")
        ]
    ),
    (
        "Familiar in Oracle ERP, SAP and SQL",
        [
            (32, 35, "programming")
        ]
    ),
    (
        "Undergraduate degree in Computer Science or Information Technology",
        [
            (0, 13, "degree"),
            (24, 40, "major"),
            (44, 66, "major")
        ]
    ),
    (
        "Experience with, or common knowledge and familiarity of Microsoft technology (e.g., SQL Database, .NET or Azure knowledge, O365, MS Flow, Power BI and Power App platform solution)",
        [
            (84, 87, "programming"),
            (98, 102, "programming"),
            (106, 111, "cloud"),
            (138, 146, "BI")
        ]
    ),
    (
        "SDLC and project management experience in large scale system revamp projects",
        []
    ),
    (
        "Familiarity with AWS, Git, Airflow is a plus",
        [
            (17, 20, "cloud"),
        ]
    ),
    (
        "Experience in using Tableau, Power BI or related analytics visualization tools would be an advantage",
        [
            (20, 27, "BI"),
            (29, 37, "BI")
        ]
    ),
    (
        "Good command of Python or R",
        [
            (16, 22, "programming"),
            (26, 27, "programming")
        ]
    ),
    (
        "Hand-on knowledge in SQL or other data manipulation languages",
        [
            (21, 24, "programming")
        ]
    ),
    (
        "Bachelor degree or equivalent in Data Analytics, Computer Science, Information Management, Mathematics, Statistics, or related disciplines",
        [
            (0, 8, "degree"),
            (33, 47, "major"),
            (49, 65, "major"),
            (67, 89, "major"),
            (91, 102, "major"),
            (104, 114, "major")
        ]
    ),
    (
        "Degree holder preferably an engineering or IT background",
        [
            (28, 39, "major"),
            (43, 45, "major")
        ]
    ),
    (
        "Knowledge in programming languages like SQL, R, and Python.",
        [
            (40, 43, "programming"),
            (45, 46, "programming"),
            (52, 58, "programming")
        ]
    ),
    (
        "Proficient in statistics and statistical packages like Excel",
        [
            (55, 60, "BI")
        ]
    ),
    (
        "Bachelor’s degree in related field - Business, Data Analytics, statistics, mathematics",
        [
            (0, 8, "degree"),
            (37, 45, "major"),
            (47, 61, "major"),
            (63, 73, "major"),
            (75, 86, "major")
        ]
    ),
    (
        "Bachelor degree of Information Technology/ Computer Science or any related discipline;",
        [
            (0, 8, "degree"),
            (19, 41, "major"),
            (43, 59, "major")
        ]
    ),
    (
        "Experience in Tableau, PowerBI, SSAS, Azure SQL server, Azure -Data warehouse and Data Factory is a plus",
        [
            (14, 21, "BI"),
            (23, 30, "BI"),
            (38, 43, "cloud"),
            (56, 61, "cloud")
        ]
    ),
    (
        "Hold a relevant Bachelors or Masters degree in Computer Science, Business Analytics, Engineering or similar",
        [
            (16, 25, "degree"),
            (29, 36, "degree"),
            (47, 63, "major"),
            (65, 83, "major"),
            (85, 96, "major")
        ]
    ),
    (
        "Good knowledge of Python programming is required",
        [
            (18, 24, "programming")
        ]
    ),
    (
        "Knowledge of SQL and database systems is a plus",
        [
            (13, 16, "programming")
        ]
    ),
    (
        "Knowledge of a BI solution is preferred (Microsoft BI, Tableau, Tibco Spotfire, Qlik View, etc.)",
        [
            (55, 62, "BI"),
            (64, 78, "BI"),
            (80, 84, "BI")
        ]
    ),
    (
        "Statistical and data mining techniques like GLM/Regression, Random Forest, Boosting, Trees etc.",
        []
    ),
    (
        "Web services: Redshift, S3, Athena etc.",
        [
            (14, 22, "cloud"),
            (24, 26, "cloud"),
            (28, 34, "cloud")
        ]
    ),
    (
        "Data/database tools: Excel, MySQL/PostgreSQL etc.",
        [
            (21, 26, "BI"),
            (28, 33, "DB"),
            (34, 44, "DB")
        ]
    ),
    (
        "Knowledge of statistics and experience using statistical packages (R, Python etc)",
        [
            (67, 68, "programming"),
            (70, 76, "programming")
        ]
    ),
    (
        "Proficiency in SQL, VBA, Access",
        [
            (15, 18, "programming"),
            (20, 23, "programming"),
            (25, 31, "DB")
        ]
    ),
    (
        "Knowledge of Tableau or Robotic Process Automation (RPA) will be a plus.",
        [
            (13, 20, "BI"),
        ]
    ),
    (
        "Strong knowledge in ASP.Net Framework, C#, SQL tools, Reporting tools,",
        [
            (20, 27, "programming"),
            (39, 41, "programming"),
            (43, 46, "programming")
        ]
    ),
    (
        "Good computer skills (especially Excel); Other programming language such as python is a plus.",
        [
            (33, 38, "BI"),
            (76, 82, "programming")
        ]
    ),
    (
        "Proficient in using analytics tools like VBA, SQL, Python, SAS, or other programming language",
        [
            (41, 44, "programming"),
            (46, 49, "programming"),
            (51, 57, "programming"),
            (59, 62, "programming")
        ]
    ),
    (
        "Proficient in at least two of following programming skills: PL/SQL, Hive SQL, Java, Spark/Flink and Python",
        [
            (60, 66, "programming"),
            (78, 82, "programming"),
            (100, 106, "programming")
        ]
    ),
    (
        "Exposure in BI/reporting systems would be an advantage such as Tableau, PowerBI etc.",
        [
            (63, 70, "BI"),
            (72, 79, "BI")
        ]
    ),
    (
        "Additional knowledge in programming language like R or Python is good value add",
        [
            (50, 51, "programming"),
            (55, 61, "programming")
        ]
    ),
    (
        "Hands-on development skills in C#, ASP.NET, VB.NET and MSSQL",
        [
            (31, 33, "programming"),
            (35, 42, "programming"),
            (44, 50, "programming"),
            (55, 60, "programming")
        ]
    ),
    (
        "Proficient in Python within the PyData stack (Pandas, Numpy, Matplotlib)",
        [
            (14, 20, "programming")
        ]
    ),
    (
        "Experienced with data presentation tools such as Tableau, to clearly articulate the outputs, conclusions and weaknesses of your models to both technical and non-technical stakeholders",
        [
            (49, 56, "BI")
        ]
    ),
    (
        "Knowledge in PowerBI, SQL, Python, PHP, Javascript is advantage ",
        [
            (13, 20, "programming"),
            (22, 25, "programming"),
            (27, 33, "programming"),
            (35, 38, "programming"),
            (40, 50, "programming")
        ]
    ),
    (
        "Proficient in Google Analytics, Google Data Studio, SQL, Firebase, Advanced level of MS Excel, R / Python",
        [
            (14, 30, "BI"),
            (32, 50, "BI"),
            (52, 55, "programming"),
            (88, 93, "BI"),
            (95, 96, "programming"),
            (99, 105, "programming")
        ]
    ),
    (
        "Bachelor’s Degree in Electronics Engineering; MBA is an added advantage",
        [
            (0, 8, "degree"),
            (21, 44, "major")
        ]
    ),
    (
        "Strong knowledge of and experience with reporting packages (Business Objects etc), databases (SQL etc), programming (XML, Javascript, or ETL frameworks)",
        [
            (94, 97, "programming"),
            (117, 120, "programming"),
            (122, 132, "programming")
        ]
    ),
    (
        "Proficient in visualization tools e.g. Tableau/ PowerBI is desirable",
        [
            (39, 46, "BI"),
            (48, 55, "BI")
        ]
    ),
    (
        "Minimum 8 years of experience working with complex TSQL queries, SSIS and SSAS. SSRS/Power BI experience is required. (designing stored procedures, triggers, tables, extensions)",
        [
            (51, 55, "programming"),
            (85, 93, "BI")
        ]
    ),
    (
        "Bachelor’s degree in computer science, information systems or engineering or equivalent technology domain experience",
        [
            (0, 8, "degree"),
            (21, 37, "major"),
            (39, 58, "major"),
            (62, 73, "major")
        ]
    ),
    (
        "Good programming skills, for example, JavaScript, Node.js, Java, .NET, PHP, Python OR other programming languages.",
        [
            (38, 48, "programming"),
            (50, 57, "programming"),
            (59, 63, "programming"),
            (65, 69, "programming"),
            (71, 74, "programming"),
            (76, 82, "programming")
        ]
    ),
    (
        "Experiences in Scrum/Agile/Waterfall would be an advantage. ",
        [
        ]
    ),
    (
        "Conceptual knowledge of HTML would be an advantage ",
        [
            (24, 28, "programming")
        ]
    ),
    (
        "Experience with Azura Data Factory, Data Lake, Big Data, BI Dashboard by PowerBI / Qlik",
        [
            (16, 21, "cloud"),
            (73, 80, "BI"),
            (83, 87, "BI")
        ]
    ),
    (
        "Knowledge in in Azure, SOAP, Microsoft SQL Server, Oracle and MySQL a definitively advantage",
        [
            (16, 21, "cloud"),
            (29, 49, "DB"),
            (51, 57, "DB"),
            (62, 67, "DB")
        ]
    ),
    (
        "Experience with NoSQL databases (e.g., MongoDB)",
        [
            (39, 46, "DB")
        ]
    ),
    (
        "Bachelors or Masters degree in Mathematics, Statistics, Physics, Computer Science, or another highly quantitative field",
        [
            (0, 9, "degree"),
            (13, 20, "degree"),
            (31, 42, "major"),
            (44, 54, "major"),
            (65, 81, "major")
        ]
    ),
    (
        "Experience with translating mathematical models and algorithms into code (Python, R or C++)",
        [
            (74, 80, "programming"),
            (82, 83, "programming"),
            (87, 90, "programming")
        ]
    ),
    (
        "Proficiency in using SQL, OLAP cubes, Access and VBA, other MS office applications, especially in Excel is a MUST",
        [
            (21, 24, "programming"),
            (38, 44, "DB"),
            (49, 52, "programming"),
            (98, 103, "BI")
        ]
    ),
    (
        "Strong programming skill is essential and technical proficiency in at least one of below languages: Python, Matlab, R; C++, Java and C# is a plus",
        [
            (100, 106, "programming"),
            (108, 114, "programming"),
            (116, 117, "programming"),
            (119, 122, "programming"),
            (124, 128, "programming"),
            (133, 135, "programming")
        ]
    ),
    (
        "Experience working with big data infrastructure tools such as Hive, HDFS, HBase, Python, SQS, Scala, Spark, Java",
        [
            (81, 87, "programming"),
            (94, 99, "programming"),
            (108, 112, "programming")
        ]
    ),
    (
        "Bachelors degree or higher in Computer Science, Mathematics, EE or other computational discipline from a top tier university.",
        [
            (0, 9, "degree"),
            (30, 46, "major"),
            (48, 59, "major"),
            (61, 63, "major")
        ]
    ),
    (
        "Strong understanding of database technology and best practice, experience in MSSQL and MySQL is required, Oracle is a plus",
        [
            (77, 82, "DB"),
            (87, 92, "DB"),
            (106, 112, "DB")
        ]
    ),
    (
        "Good command of SQL, Excel, VBA, Powerpoint, Access. Knowledge in Python or Tableau an advantage",
        [
            (16, 19, "programming"),
            (21, 26, "BI"),
            (28, 31, "programming"),
            (45, 51, "DB"),
            (66, 72, "programming"),
            (76, 83, "BI")
        ]
    ),
    (
        "Bachelor’s degree in Information Technology, Computer Science, Business Administration, Economics, Statistics or related disciplines",
        [
            (0, 8, "degree"),
            (21, 43, "major"),
            (45, 61, "major"),
            (63, 86, "major"),
            (88, 97, "major"),
            (99, 109, "major")
        ]
    ),
    (
        "Hong Kong (IAP/PRW259/21) Hong Kong",
        [

        ]
    ),
    (
        "Solid experience in developing applications using one or more of the following: Java, C#, ASP.NET, HTML, JavaScript, CSS and SQL",
        [
            (80, 84, "programming"),
            (86, 88, "programming"),
            (90, 97, "programming"),
            (99, 103, "programming"),
            (105, 115, "programming"),
            (117, 120, "programming"),
            (125, 128, "programming")
        ]
    ),
    (
        "Technical Manager/Assistant Technical Manager/Senior Technical Officer/Technical Officer (holding the functional title of Data Scientist or Data Analyst) in the School of Public Health",
        [

        ]
    ),
    (
        "A highly competitive salary commensurate with qualifications and experience will be offered, in addition to annual leave and medical benefit. The appointment on fixed term will attract a contract-end gratuity and University contribution to a retirement benefits scheme, totalling up to 10% of basic salary.",
        [

        ]
    ),
    (
        "Applicants should possess a Bachelor’s degree or above in statistics, biostatistics, computer science, mathematics, informatics, data science or a related discipline, with at least 3 years’ relevant work experience. They should have a strong quantitative background; experience in analysing epidemiological data using R, STATA, SAS or other statistical packages; and demonstrated expertise in the analysis of large and complex datasets. They should also have excellent written and oral communication skills; strong data visualization skills; the ability to work independently as well as in a multidisciplinary team; and the ability to acquire new statistical techniques by self-learning. They should be organised, responsible, resourceful, attentive to details, and able to multi-task and present abstract concepts in an accessible way to audiences of different backgrounds. Proficiency in longitudinal analyses, and knowledge of multilevel modelling, and state-of-the-art statistical and epidemiological models would be advantages.",
        [
            (28, 36, "degree"),
            (58, 68, "major"),
            (70, 83, "major"),
            (85, 101, "major"),
            (103, 114, "major"),
            (116, 127, "major"),
            (129, 141, "major"),
            (318, 319, "programming"),
            (321, 326, "programming"),
            (328, 331, "programming")
        ]
    ),
    (
        "The appointee will be primarily responsible for the applied and methodological work in epidemiological and/or statistical research, and work with a large population-based cohort with over 46,000 participants in 20,000 households. He/She will conduct power/sample size estimation; generate tables and figures for reports and presentations; contribute to scientific publications, grant proposals and reports; and perform general administrative, operational and other duties as assigned. Enquiries about the duties of the post should be sent to familyco@hku.hk. Information about the School can be obtained at http://sph.hku.hk/index.php. Those who have responded to the previous advertisement (Ref.: 508356) need not re-apply.",
        [

        ]
    ),
    (
        "Aon Plc is a leading global professional services firm providing a broad range of risk, retirement and health solutions. Our 50,000 colleagues in 120 countries empower results for clients by using proprietary data and analytics to deliver insights that reduce volatility and improve performance",
        [

        ]
    ),
    (
        "Data & Analytics Consultant",
        [

        ]
    ),
    (
        "Lloyd Karson is an international leading provider of permanent recruitment, contract professionals and talent management services worldwide.We assists corporations in identifying, assessing and recruiting mid-level management to senior executive talent across various industries. With our headquarter in Australia, we are expanding our business reach across Asia Pacific. \n ",
        [

        ]
    ),
    (
        "The Hong Kong office specializes in human resources & business support, information technology, sales & marketing, accounting & finance, property & construction, supply chain, and logistics & procurement.",
        [

        ]
    ),
    (
        "Technical experience in using Microsoft Azure, Microsoft SQL Server, SSIS, SSRS and Mircosoft tools and Power BI",
        [
            (40, 45, "cloud"),
            (47, 67, "DB"),
            (104, 112, "BI")
        ]
    ),
    (
        "(Ref.: 512217) (to commence as soon as possible on a one-year temporary basis or two-year fixed-term basis, with the possibility of renewal subject to satisfactory performance)",
        [

        ]
    ),
    (
        "Yrs of Total Post-Quali Exp 2.0 Requirements - With data analysis / business intelligence background (using Tableau, Qlikview, PowerBI, hyperion, Cognos, etc.)",
        [
            (108, 115, "BI"),
            (117, 125, "BI"),
            (127, 134, "BI"),
            (136, 144, "BI"),
            (146, 152, "BI")
        ]
    ),
    (
        "Prepare sales contract / PO / invoice / delivery note / packing list, etc",
        [

        ]
    ),
    (
        "Shipping Clerk (with L/C experience)",
        [

        ]
    ),
    (
        "Min. 3 years’ experience preferably in logistics or shipping industries, candidate with less experience and fresh graduate will also be considered",
        [

        ]
    ),
    (
        "Minimum 1 years of relevant experience in data analysis; with strong computer skills in Excel/ Visual Basic/ Access Macro",
        [
            (88, 93, "BI"),
            (109, 115, "DB")
        ]
    ),
    (
        "Provide P & L and budgeting reports for management team",
        [

        ]
    ),
    (
        "Design, plan and evaluate experiments to get actionable insights and to grow business performance. Yrs of Total Post-Quali Exp 5.0 Requirements - BA/BS in Data Analysis, Economics, Math, Physics, Computing, Statistics, Business Administration, or other relevant subjects;",
        [
            (146, 148, "degree"),
            (149, 151, "degree"),
            (155, 168, "major"),
            (170, 179, "major"),
            (181, 185, "major"),
            (187, 194, "major"),
            (196, 205, "major"),
            (207, 217, "major"),
            (219, 242, "major")
        ]
    ),
    (
        "Utilize available data to generate reports, analysis and interpret into business terms via data visualisation tools",
        [

        ]
    ),
    (
        "(Senior) Data Analyst - Local conglomerate, 30-40k Perm",
        [

        ]
    ),
    (
        "Discover and build practice with new technology and partners from the market, with special focus on: A.I. / Data Analytics / Video Analytics / IoT / Cloud / Blockchain",
        [

        ]
    ),
    (
        "Good understanding on the prevalent NLP-related algorithms and models like Word2Vec, LSTM, Transformer, GPT, Bert etc.",
        []
    ),
    (
        "Have experience with Azure and Databricks will be a plus.",
        [
            (21, 26, "cloud"),
        ]
    ),
    (
        "ION Analytics’ solutions include Acuris, Dealogic, Infralogic and Selerity, and is part of the rapidly expanding ION Group.",
        [

        ]
    ),
    (
        "We have an opportunity available at Infralogic, part of the ION Analytics division of the ION Group. ION Analytics is a provider of business intelligence, with niche products which cover public and private M&A, distressed debt and infrastructure, to name a few. Infralogic is the only analytical platform that helps infrastructure investment professionals originate new business by quickly gaining insights into the market. Our major offices are in London, New York, Hong Kong and Mumbai. We are looking for an Editorial Research Analyst for our Hong Kong office. The Editorial Research Analyst will gather, process and systematize data and report on new market developments.",
        [

        ]
    ),
    (
        "Deep understanding of Machine Learning concepts and algorithms (e.g. predictive modeling, clustering, NLP, Computer Vision, etc)",
        []
    ),
    (
        "You will consistently engage with Head / C-level stakeholders directly on your innovative idea & Data Science solutions",
        [

        ]
    ),
    (
        "Data Science Analyst / Assistant Data Science Analyst (1-year contract)",
        [

        ]
    ),
    (
        "to join our Technology Consulting – Data and Analytics (DnA) team in our Hong Kong office.",
        [

        ]
    ),
    (
        "Hands-on experience in data analytics with Tableau / Spotfire / Power BI",
        [
            (43, 50, "BI"),
            (53, 61, "BI"),
            (64, 72, "BI")
        ]
    ),
    (
        "To work closely with ISD on projects delivery and first line support on production issues",
        [

        ]
    ),
    (
        "Familiar with SQL Server / MySQL / pgSQL, Azure product and service (Blob Storage / Data Catalog / Data Factory / Data Warehouse / Power BI / etc.)",
        [
            (14, 24, "DB"),
            (27, 32, "DB"),
            (35, 40, "DB"),
            (42, 47, "cloud"),
            (131, 139, "BI")
        ]
    ),
    (
        "Bachelor’s degree in Mathematics / Statistics / Computer Science or other relevant discipline",
        [
            (0, 8, "degree"),
            (21, 32, "major"),
            (35, 45, "major"),
            (48, 64, "major")
        ]
    ),
    (
        "Familiar with SQL, Spark, Spotfire, Python, R",
        [
            (14, 17, "programming"),
            (26, 34, "BI"),
            (36, 42, "programming"),
            (44, 45, "programming")
        ]
    ),
    (
        "Experience with Azura Data Factory, Data Lake, Big Data, BI Dashboard by PowerBI / Qlik",
        [
            (16, 21, "cloud"),
            (73, 80, "BI"),
            (83, 87, "BI")
        ]
    ),
    (
        "Minimum 3 years IT working experience, must have 1+ years hands-on experience in BI reporting ",
        [

        ]
    ),
    (
        "Oracle DB, SQL / PL SQL",
        [
            (0, 9, "DB"),
            (11, 14, "programming"),
            (17, 23, "programming")
        ]
    ),
    (
        "Oracle DB, PL SQL, Python, Big Data, Cloud Data Warehouse",
        [
            (0, 9, "DB"),
            (11, 17, "programming"),
            (19, 25, "programming")
        ]
    ),
    (
        "Post date: 25 March 2022",
        [

        ]
    ),
    (
        "5 days, 14 days AL, CWB",
        [

        ]
    ),
    (
        "or corrine.chan@hays.com.hk now. If this job isn't quite right for you but you are looking for a new position, please contact us for a confidential discussion on your career. #1215013",
        [

        ]
    ),
    (
        "Proficient in at least one high level programming languages such (i.e. Python,, Pyspark, AWS solutions, Julia, and etc.)",
        [
            (71, 77, "programming"),
            (89, 92, "cloud"),
            (104, 109, "programming")
        ]
    ),
    (
        "DSE English Level 4 or above / IELTS Writing Band 7 or above preferred",
        [

        ]
    ),
    (
        "Collaborate with business users and IT to perform data analysis / data mining to support business objectives such as marketing campaign management",
        [

        ]
    ),
    (
        "hands on experience in design using more than one of these is a must - SQL, Excel Macro, Alteryx, Tableau and Python.",
        [
            (71, 74, "programming"),
            (76, 87, "programming"),
            (89, 96, "BI"),
            (98, 105, "BI"),
            (110, 116, "programming")
        ]
    ),
    (
        "relevant experience of 2-5 years in Wealth Management risk controls/data investigation related execution.",
        [
                
        ]
    ),
    (
        "250360BR",
        [

        ]
    ),
    (
        "Development experience in at least one scripting language (Python, PHP, Perl, etc.).Strong analytical and problem-solving skills; ability to transform data into business insights and actionable recommendations.",
        [
            (59, 65, "programming"),
            (67, 70, "programming"),
            (72, 76, "programming")
        ]
    ),
    (
        "Bachelor's or Master’s degree in an analytical field or similar.1+ years of work experience in doing finance/business/risk data analysis.",
        [
            (0, 8, "degree"),
            (14, 20, "degree")
        ]
    ),
    (
        "Lalamove is looking for an experienced Data Analyst to support our Risk team. The role entails driving analytics insights and enabling senior leadership to make effective, analytically driven decisions, in particular areas of fraud risk and financial efficiency. The ideal candidate should be passionate about Lalamove and e-commerce, has a strong analytical and consultative mindset, deep understanding of databases and data visualization, the ability to thrive in a dynamic, fast-paced environment delivering against tight deadlines, and a passion for scaling operations through automation.",
        [

        ]
    ),
    (
        "Reporting directly to the Senior Manager (Analytics and Business Intelligence) and Manager (Planning and Performance), the appointee supports institutional planning and decision-making through using statistical and trend datasets to inform strategic decision making and support the endeavour to drive a data quality culture throughout the university. The appointee contributes through ensuring data governance policies, procedures and best practices are rolled out in the University.",
        [

        ]
    ),
    (
        "Sound understanding of capital market products, front to back platform architecture and systems",
        [

        ]
    ),
    (
        "ProJOB21 is a home grown recruitment firm established in 2000, and since then we are proud to be partnering with the most reputable clients from fortune 500 companies including luxury retail and notable consumer brands, as well as high profile private banks & asset management; private equity & CIBM. Our business philosophy is rooted in the concept of Integrity, Pragmatism, and Caring to our candidates and clients, our team, and our local community. ",
        [

        ]
    ),
    (
        "***Please forward your CV (word format) with present and expected salary to cv @recruithk.net",
        [

        ]
    ),
    (
        "Working knowledge of data science programing languages is required (such as R, Python, SQL, Scala)",
        [
            (76, 77, "programming"),
            (79, 85, "programming"),
            (87, 90, "programming"),
            (92, 97, "programming")
        ]
    ),
    (
        "Hands-on development experience using Java, Stored Procedures, PL/SQL, and Linux/Unix shell script. Knowledge of QlikSense, Tableau, PowerBI, and/or statistical package such as SAS, Alteryx will be an advantage;",
        [
            (38, 42, "programming"),
            (63, 69, "programming"),
            (86, 91, "programming"),
            (113, 122, "BI"),
            (124, 131, "BI"),
            (133, 140, "BI"),
            (177, 180, "programming"),
            (182, 189, "BI")
        ]
    ),
    (
        "Please note that with effect from 1 June 2022 onwards, all Cathay employees and contractors who work in Cathay City and all other Cathay Group Company premises in Hong Kong must have received a third dose of COVID 19 vaccine. Being tested regularly for COVID-19 is not an option. Consideration will be given to those who are unable to get vaccinated for valid medical reasons.",
        [

        ]
    ),
    (
        "03 Jun 2022",
        [

        ]
    ),
    (
        "As a Junior Data Scientist/ Analyst, this is an excellent opportunity for you to work on projects with seniors that provide data-driven insights for business decisions.",
        [

        ]
    ),
    (
        "Either experience on Java or C#, .NET, Android/ iOS, Angular / NodeJS / ReactJS /machine learning python programming are welcome",
        [
            (21, 25, "programming"),
            (29, 31, "programming"),
            (33, 37, "programming"),
            (53, 60, "programming"),
            (63, 69, "programming"),
            (72, 79, "programming"),
            (98, 104, "programming")
        ]
    ),
    (
        "Support UAT, prepare user manual and conduct training",
        [

        ]
    ),
    (
        "Develop, design and facilitate swift delivery and distribution of analytical output across different functions (front office to support & control) in WM APAC",
        [

        ]
    ),
    (
        "Proudly serving over 3 million customers, PC Financial continues to grow by offering payment solutions and services that reward our customers every day. As a subsidiary of Loblaws Company Inc., we share the CORE values of Care, Ownership, Respect and Excellence. We are dedicated to helping Canadians Live Life Well. Join us on our journey.",
        [

        ]
    ),
    (
        "500 Lakeshore Blvd. West, Toronto, Ontario, M5V 2V9",
        [

        ]
    ),
    (
        "Hands on with SAS. Experience with Python is a bonus.",
        [
            (14, 17, "programming"),
            (35, 41, "programming")
        ]
    ),
    (
        "Experience with BI tools and Cloud technology, such as Tableau and Google Cloud Platform.",
        [
            (55, 62, "BI"),
            (67, 88, "cloud")
        ]
    ),
    (
        "About IDC: International Data Corporation (IDC) is the premier global provider of market intelligence, advisory services, and events for the information technology, telecommunications and consumer technology markets. IDC helps IT professionals, business executives, and the investment community make fact-based decisions on technology purchases and business strategy. More than 1,100 IDC analysts provide global, regional, and local expertise on technology and industry opportunities and trends in over 110 countries worldwide. For 50 years, IDC has provided strategic insights to help our clients achieve their key business objectives. IDC is a subsidiary of IDG, the world's leading technology media, research, and events company.",
        [

        ]
    ),
    (
        "Experience with SQL, SAS, Teradata, and data visualization tools",
        [
            (16, 19, "programming"),
            (21, 24, "programming"),
            (26, 34, "DB")
        ]
    ),
    (
        "#Indeed #Bi #BusinessIntelligence #Dashboards #AI #MachineLearning #Tech #Technology #Analytics #SQL #SAS #Teradata",
        [

        ]
    ),
    (
        "#EmployeeReferralProgram #ProgrammeRecommandationEmployes",
        [

        ]
    ),
    (
        "Job Location: Canada : Ontario : Toronto || Canada : Quebec : Montreal",
        [

        ]
    ),
    (
        "Job Status: Regular - Full Time",
        [

        ]
    ),
    (
        "TORONTO, Ontario, Canada",
        [

        ]
    ),
    (
        "2022-06-06-07:00",
        [

        ]
    ),
    (
        "Experience with SQL/Teradata or other database management systems",
        [
            (16, 19, "programming"),
            (20, 28, "DB")
        ]
    ),
    (
        "As an Analyst – Sales Force Analytics at a Major Financial Institution, you will help with the development and delivery of the quality assurance strategy for Distribution Reporting for Financial Planners. You will also be accountable in helping develop and implement test plans for reporting enhancements and new report builds, and ensuring that outputs support the strategic pillars of the Canadian Personal & Commercial lines of business. The successful candidate will manage an intake system, including related communication with stakeholders and collaboration with Reporting Managers for the Mortgage Specialist Sales Force. You will combine both business and technology acumen to develop a robust quality assurance infrastructure for the broader Sales Force Analytics & Optimization team.",
        [

        ]
    ),
    (
        "Ability to write and create advanced formulas using VLOOKUP, Arrays, Index and Match functions; debug and audit",
        [

        ]
    ),
    (
        "Understanding and usage of SQL keywords, data types, constraints, pivots, sub queries, logical and comparison operators, and advanced joins (inner, outer) and unions",
        [
            (27, 30, "programming")
        ]
    ),
    (
        "You can build and run a linear regression model in Excel or Python and are able to explain things such as R square, P-value, or regression coefficients to an audience that has no background in statistics.",
        [
            (51, 56, "BI"),
            (60, 66, "programming"),
        ]
    ),
    (
        "Certificate in Big Data and Advanced Data Analytics with exposure of cloud data solutions (specifically MS Azure and Power BI) is an asset.",
        [
            (107, 112, "cloud"),
            (117, 125, "BI")
        ]
    ),
    (
        "Good working knowledge of R, Python, Business Intelligence tools (e.g. Power BI, Tableau)",
        [
            (26, 27, "programming"),
            (29, 35, "programming"),
            (71, 79, "BI"),
            (81, 88, "BI")
        ]
    ),
    (
        "Strong in SQL, Big Query and Power Query is a must, Python is a plus.",
        [
            (10, 13, "programming"),
            (15, 24, "cloud"),
            (52, 58, "programming")
        ]
    ),
    (
        "Gannett Co., Inc. is a proud equal opportunity employer committed to building and maintaining a diverse workforce. As such, we will consider all qualified applicants for employment and do not discriminate in connection with employment decisions on the basis of an applicant or employee’s race, color, national origin, ethnicity, ancestry, citizenship status, sex, gender, gender identity, gender expression, religion, age, marital status, personal appearance (including height and weight), sexual orientation, family responsibilities, physical or mental disability, medical condition, pregnancy status (including childbirth, breastfeeding or related medical conditions), education, genetic characteristics or information, political affiliation, military or veteran status or other classifications protected by applicable federal, state and local laws in the jurisdictions where Gannett employs employees. In addition, Gannett Co., Inc. will provide applicants who require a reasonable accommodation, as a result of an applicant’s disability or religion, to complete this employment application and/or any other process in connection with an individuals’ application for employment with Gannett Co., Inc. Applicants who require such accommodation should contact Gannett Co., Inc.’s Recruitment Department at Recruit@gannett.com.",
        [

        ]
    ),
    (
        "Data analytics / ETL / SQL / BI",
        [

        ]
    ),
    (
        "Familiarity with tools like JIRA and Confluence",
        [
        ]
    ),
    (
        "Hands-on experience with various SDLC including waterfall, agile and extreme methodologies",
        [
        ]
    ),
    (
        "Join in on what others in TD Technology Solutions are doing:",
        [

        ]
    ),
    (
        "Developing efficient DAX queries for KPI calculations",
        [

        ]
    ),
    (
        "Have expertise in SQL (we use Postgres + Snowflake) and event-based ",
        [
            (18, 21, "programming"),
            (30, 38, "DB"),
            (41, 50, "cloud")
        ]
    ),
    (
        "Nice to haves: Airflow, other DAG tool experience, Python, Node",
        [
            (51, 57, "programming"),
            (59, 63, "programming")
        ]
    ),
    (
        "3+ years in relevant technical area, including administration of BI, ML and ETL applications",
        [

        ]
    ),
    (
        "Experience with DataRobot, Snowflake, Wherescape, Alteryx, KNIME, Tableau or Power Platform",
        [
            (16, 25, "cloud"),
            (27, 36, "cloud"),
            (50, 57, "BI"),
            (59, 64, "BI"),
            (66, 73, "BI")
        ]
    ),
    (
        "Strong understanding of Windows/Linux OS, basic networking, and application servers",
        []
    ),
    (
        "Experience with implementing CI/CD pipelines in a large data warehouse environment",
        [
        ]
    ),
    (
        "Advanced experience with Excel, Access, Tableau, SQL and SharePoint with an understanding of R, Python, Azure Databricks or other programing languages",
        [
            (25, 30, "BI"),
            (32, 38, "DB"),
            (40, 47, "BI"),
            (49, 52, "programming"),
            (93, 94, "programming"),
            (96, 102, "programming"),
            (104, 109, "cloud"),
        ]
    ),
    (
        "Manage lesson planning, assignments, class, and overall course assessment of the students’ work while ensuring students’ awareness of course objectives and TSoM’s expectations.",
        [

        ]
    ),
    (
        "Experience supporting MySQL / Percona Server / MariaDB in a production environment, with in-depth knowledge of topics such as MySQL backups, high availability, and performance tuning",
        [
            (22, 27, "DB"),
            (30, 37, "cloud"),
            (47, 54, "DB"),
            (126, 131, "DB")
        ]
    ),
    (
        "Fluency in SQL, Python, Bash, or other scripting languages",
        [
            (11, 14, "programming"),
            (16, 22, "programming"),
            (24, 28, "programming")
        ]
    ),
    (
        "Big data, Hadoop, support experience/ Data engineers who is ok to work for support",
        [
        ]
    ),
    (
        "Knowledge of data visualization tools and techniques (Tableau, PowerBI, Looker, etc.).",
        [
            (54, 61, "BI"),
            (63, 70, "BI"),
            (72, 78, "BI")
        ]
    ),
    (
        "Works with support teams (i.e. Sprint, Cloud Operations, Cloud Assurance, InfoSec), to drive the release(s) of various applications in non-production and production environments.",
        [

        ]
    ),
    (
        "AWS Cloud tools/technologies: S3, EMR, EC2, Lambda.",
        [
            (0, 3, "cloud")
        ]
    ),
    (
        "Experience in any DWH-on-Cloud solution like Redshift, Snowflake etc.",
        [
            (45, 53, "cloud"),
            (55, 64, "cloud")
        ]
    ),
    (
        "Experience in Cloudera CDP, PySpark, Spark SQL, Hive, Hadoop",
        [
            (14, 22, "cloud"),
            (43, 46, "programming"),
        ]
    ),
    (
        "Understanding of Docker concepts and container orchestration",
        [
        ]
    ),
    (
        "Knowledge of Linux, SQL, RDBMS (SQL Server, Oracle etc) and shell scripting",
        [
            (20, 23, "programming"),
            (32, 42, "DB"),
            (44, 50, "DB"),
            (60, 65, "programming")
        ]
    ),
    (
        "Expert understanding of cloud, databases / data warehouse, infrastructure, architecture, DevSecOps and application development / engineering",
        [

        ]
    ),
    (
        "Demonstrate experience with languages such as Python, Bash, Powershell",
        [
            (46, 52, "programming"),
            (54, 58, "programming"),
            (60, 70, "programming")
        ]
    ),
    (
        "Although this position is not about keeping our data pipeline running, you will be writing Airflow ETLs",
        [
        ]
    ),
    (
        "Hand On experience with tools like Jira, HP ALM, Bitbucket/GIT, Jenkins.",
        [
        ]
    ),
    (
        "Knowledge on XML and build scripts like Ant, logging mechanisms like log4j, slf4j",
        [
            (13, 16, "programming"),
            (40, 43, "programming")
        ]
    ),
    (
        '''
        JOB TYPE: Freelance, Contract Position (no agencies/C2C - see notes below)
        LOCATION: Remote Work from anywhere Work anytime
        HOURLY RANGE: Our client is looking to pay $40 – $65 /hr
        ESTIMATED DURATION: 40h/week - long-term, ongoing project 
        ''',
        [

        ]
    ),
    (
        "Knowledge and experience in Web3/DeFi Protocols/Blockchain",
        [

        ]
    ),
    (
        "Strong knowledge of Python, Spark, and SQL",
        [
            (20, 26, "programming"),
            (39, 42, "programming")
        ]
    ),
    (
        '''
        Have experience with Kafka Streams SDK
        Have experience with various Akka frameworks (including Streams and HTTP)
        Have experience building DataDog dashboards for application monitoring
        Know Unix well
        Have public examples of projects you’ve completed
        Have published technically relevant articles, blog posts or books
        ''',
        [

        ]
    ),
    (
        "Have worked on a scrum team",
        [
        ]
    ),
    (
        "Experience with data processing frameworks such as Apache Spark",
        [
        ]
    ),
    (
        "Experience with data warehouses like Amazon Redshift or Snowflake",
        [
            (37, 43, "cloud"),
            (44, 52, "cloud"),
            (56, 66, "cloud")
        ]
    ),
    (
        "Experience with an IaC tool such as CloudFormation, Amazon CDK or Terraform",
        [
            (36, 50, "cloud"),
            (52, 62, "cloud"),
            (66, 75, "cloud")
        ]
    ),
    (
        "Demonstrated data storage knowledge of SQL Server, Cosmos DB, and Data Lakes",
        [
            (39, 49, "DB"),
            (51, 60, "DB")
        ]
    ),
    (
        "Knowledge of Excel ETL features such as Power Query",
        [
            (13, 18, "BI")
        ]
    ),
    (
        "As a top 10 North American bank, our client aims to stand out from its peers by having a differentiated brand - anchored in a proven business model and rooted in a desire to give its customers, communities, and colleagues the confidence to thrive in a changing world.",
        [

        ]
    ),
    (
        "Expert in Microsoft Office- Excel, Word, Visio and PowerPoint, VBA / Macros",
        [
            (28, 33, "BI"),
            (63, 66, "programming"),
            (69, 75, "programming")
        ]
    ),
    (
        "Experience with analytics databases (BigQuery preferred)",
        [
            (37, 45, "cloud")
        ]
    ),
    (
        "Technology involvement in at least two of these languages: Python, Node.JS, Power shell, Scripts, Java, .NET, SQL is essential.",
        [
            (59, 65, "programming"),
            (67, 74, "programming"),
            (76, 87, "programming"),
            (89, 96, "programming"),
            (98, 102, "programming"),
            (104, 108, "programming"),
            (110, 113, "programming")
        ]
    ),
    (
        "Data - Experience with SQL, and MS server data & tools are a must. Knowledge of Python, SSIS, and MS Azure cloud services (such as Azure Data Factory, Databricks, ADLS, Delta Lake, Azure SQL DB, and Azure Synapse) is a strong asset.",
        [
            (23, 26, "programming"),
            (80, 86, "programming"),
            (88, 92, "programming"),
            (101, 106, "cloud"),
            (131, 136, "cloud"),
            (141, 149, "cloud"),
            (163, 167, "cloud"),
            (169, 179, "cloud"),
            (181, 193, "cloud"),
        ]
    ),
    (
        "- Strong knowledge of SQL",
        [
            (22, 25, "programming")
        ]
    ),
    (
        "- Python experience",
        [
            (2, 8, "programming")
        ]
    ),
    (
        "Knowledge of industry best practices including: DAMA International Body of Knowledge; ARMA; IAPP.",
        [

        ]
    ),
    (
        "GCP data technologies (Google Cloud, Big Query), experience with other cloud databases such as Snowflake",
        [
            (0, 3, "cloud"),
            (23, 35, "cloud"),
            (37, 46, "cloud"),
            (95, 104, "cloud")
        ]
    ),
    (
        "Data intelligence and visualization platforms such as Looker, Google Data Studio, Tableau or other tools",
        [
            (54, 60, "BI"),
            (62, 80, "BI"),
            (82, 89, "BI")
        ]
    ),
    (
        "B.S. in Engineering, Science, Mathematics, Statistics or Computer Science.",
        [
            (0, 4, "degree"),
            (8, 19, "major"),
            (21, 28, "major"),
            (30, 41, "major"),
            (43, 53, "major"),
            (57, 73, "major")
        ]
    ),
    (
        "A recognized professional designation: IT Infrastructure Library (ITIL), Project Management Professional (PMP), Business Analysis (BA) or Information Systems Professional (ISP), etc. is an asset.",
        [

        ]
    ),
    (
        "Experience in basic coding and/or data visualization (e.g. SQL, Python, Tableau, QuickSight). If you know how to build models or write code, that’s awesome. If not, don’t worry as long as you have an interest in and aptitude for learning it.",
        [
            (59, 62, "programming"),
            (64, 70, "programming"),
            (72, 79, "BI"),
            (81, 91, "BI")
        ]
    ),
    (
        "Apply if you think we\"re a good match. We\"ll get in touch with you to let you know the next steps but in the meantime feel free to browse this: http://www.bloomberg.com/professional",
        [

        ]
    ),
    (
        "Troubleshoot model bugs, and continuously enhance and support existing models.",
        [

        ]
    ),
    (
        "Our brands include: Coca-Cola®, Diet Coke®, Coca-Cola® Zero Sugar, Sprite®, Fanta®, Barq's®, NESTEA®, POWERADE®, Minute Maid®, DASANI® and vitaminwater®; and our partner brands: Canada Dry®, Monster Energy®, and A&W®.",
        [

        ]
    ),
    (
        "Provide daily operational support to UNB maintained data centres and communication rooms. Troubleshoot, identify, and resolve low to medium complexity operational issues.",
        [

        ]
    ),
    (
        "Install and connect network, SAN, backup, and other data centre hardware by developing or applying established procedures for installation. Configure hardware, test installed equipment, and apply change management procedures to address any customizations.",
        [

        ]
    ),
    (
        "Deloitte Canada has 30 offices with representation across most of the country. We acknowledge our offices reside on traditional, treaty and unceded territories as part of Turtle Island and is still home to many First Nations, Métis, and Inuit peoples. We are all Treaty people.",
        [

        ]
    ),
    (
        "Serving a diverse urban and rural population of more than 430,000, Niagara Region is focused on building a strong and prosperous Niagara. Working collaboratively with 12 local area municipalities and numerous community partners, the Region delivers a range of high quality programs and services to support and advance the well-being of individuals, families and communities within its boundaries. Nestled between the great lakes of Erie and Ontario, the Niagara peninsula features some of Canada’s most fertile agricultural land, the majesty of Niagara Falls and communities that are rich in both history and recreational and cultural opportunities. Niagara boasts dynamic modern cities, Canada’s most developed wine industry, a temperate climate, extraordinary theatre, and some of Ontario’s most breathtaking countryside. An international destination with easy access to its binational U.S. neighbour New York State, Niagara attracts over 14 million visitors annually, as well as a steady stream of new residents and businesses.",
        [

        ]
    ),
    (
        "Proficient in Linux commands",
        []
    ),
    (
        "You are very comfortable building pivot tables in Excel or reaching similar outcomes in SQL/Python/R",
        [
            (88, 91, "programming"),
            (92, 98, "programming"),
            (99, 100, "programming")
        ]
    ),
    (
        "Monitor and track performance of CX enhancements launched, including NPS and business metrics",
        []
    ),
    (
        "Master’s or PhD in a health-related field (e.g., epidemiology, program evaluation, public health, health sciences, medicine, psychology, etc).",
        [
            (0, 6, "degree"),
            (12, 15, "degree"),
            (49, 61, "major"),
            (63, 81, "major"),
            (83, 96, "major"),
            (98, 113, "major"),
            (115, 123, "major"),
            (125, 135, "major")
        ]
    ),
    (
        "Advanced skills in Microsoft Office Suite.",
        []
    ),
    (
        "Intermediate knowledge of Python, R and next generation BI and AI, an asset",
        [
            (26, 32, "programming"),
            (34, 35, "programming")
        ]
    ),
    (
        "A Bachelor's degree in a related field, and/or commensurate work experience. Experience with fraud & risk management is strongly preferred",
        [
            (2, 10, "degree")
        ]
    ),
    (
        "3-4 years’ experience in data analytics, with experience in SQL, Python and Excel",
        [
            (60, 63, "programming"),
            (65, 71, "programming"),
            (76, 81, "BI")
        ]
    ),
    (
        "Candidates who require accommodation in the interview process may contact talentacquisition@georgebrown.ca and all information received will be addressed confidentially.",
        []
    ),
    (
        "UI/UX Design focused",
        []
    ),
    (
        "Bachelor's degree in Technical Field",
        [
            (0, 8, "degree")
        ]
    ),
    (
        "Strong in SQL, Power Query, DAX, Powershell and/or Python",
        []
    ),
    (
        "Metrolinx is connecting communities across the Greater Golden Horseshoe. Metrolinx operates GO Transit and UP Express, as well as the PRESTO fare payment system. We are also building new and improved rapid transit, including GO Expansion, Light Rail Transit routes, and major expansions to Toronto’s subway system, to get people where they need to go, better, faster and easier. Metrolinx is an agency of the Government of Ontario.",
        []
    ),
    (
        "Proficient in using AWS and/or Azure cloud platform is highly preferred.",
        [
            (20, 23, "cloud"),
            (31, 36, "cloud")
        ]
    ),
    (
        "Accountabilities are moderately complex, varied in scope and performed under direct management guidance",
        []
    ),
    (
        "Experience in NLP, Reinforcement Learning, Classification are an asset.",
        []
    ),
    (
        "Knowledge in Microsoft SQL Server and MySQL are considered assets.",
        [
            (13, 33, "DB"),
            (38, 43, "DB")
        ]
    ),
    (
        "Comfortable with managing databases such as MySQL and PostgreSQL",
        [
            (44, 49, "DB"),
            (54, 64, "DB")
        ]
    ),
    (
        "Build and supports reports using a combination of BI tools such as Power BI and SQL",
        [
            (67, 75, "BI"),
            (80, 83, "BI")
        ]
    ),
    (
        "TD Description",
        []
    ),
    (
        "At RBC, our culture is deeply supportive and rich in opportunity and reward. You will help our clients thrive and our communities prosper, empowered by a spirit of shared purpose.",
        []
    ),
    (
        "Enterprise server and virtualized infrastructure hardware, Cloud operations including GCP, Azure, OCI",
        [
            (86, 89, "cloud"),
            (91, 96, "cloud"),
            (98, 101, "cloud")
        ]
    ),
    (
        "(PowerShell, Bash, Python) ability to design the scripts utilizing API call to various secure tools",
        [
            (1, 11, "programming"),
            (13, 17, "programming"),
            (19, 25, "programming")
        ]
    ),
    (
        "Antivirus, Data Loss Prevention and Endpoint protection tools like Symantec DLP, Forcepoint, McAfee DLP. Knowledge and experience in endpoint protection and response (EDR) tools like Croudstrike, Cortex XDR, Windows Defender EDR.",
        []
    ),
    (
        "CASB technology and tools like MCAS, MVision/Skyhigh, Forcepoint",
        []
    ),
    (
        "A Wrangler: You can quickly learn to programmatically extract data from a database or an API, bring it through a transformation or two, and convert into a human-readable form (Matplotlib, d3 visualization, Tableau, etc.).",
        [
            (206, 213, "BI")
        ]
    ),
    (
        "As a creative problem-solver, you will be challenged to consider multiple options and select the optimal solution to meet the needs of your customers. You will own the recommendation and resolution to an existing business problem and will be involved end to end, from problem identification to solution deployment.",
        []
    ),
    (
        "RBC",
        []
    ),
    (
        "I",
        []
    ),
    (
        "1 Presidents Choice Circle, Brampton, Ontario, L6Y 5S5",
        []
    ),
    (
        "At Loblaw, we help millions of Canadians get through their best days, worst days, celebration days, and every day. Through our innovation and quality products, we’re here for our friends, neighbours, family members and colleagues. ",
        []
    ),
    (
        "On-site GoodLife Fitness, Basketball & Volleyball courts, Ice Rink, Groceries delivered to work via PC Express, Dry Cleaning services (1PCC Office)",
        []
    ),
    (
        "Requisition #",
        []
    ),
    (
        "1)CHRA",
        []
    ),
    (
        "Programming and scripting skills such as Python, Bash, Matlab are a must.",
        [
            (41, 47, "programming"),
            (49, 53, "programming"),
            (55, 61, "programming")
        ]
    ),
    (
        "Job ID #:",
        []
    ),
    (
        "College Diploma in Computer Science, Information System or Information Technology",
        [
            (8, 15, "degree"),
            (19, 35, "major"),
            (37, 55, "major"),
            (59, 81, "major")
        ]
    ),
    (
        "Master Data Management Analyst",
        []
    ),
    (
        "Ability to speak English and/or Oji-cree,Cree, Objibway",
        []
    ),
    (
        "Knowledge of Azure Synapse, Python, or R is an asset",
        [
            (13, 18, "cloud"),
            (28, 34, "programming"),
            (39, 40, "programming")
        ]
    ),
    (
        "Identify opportunities for optimization and A|B testing",
        []
    ),
    (
        "Familiarity with coding languages like Python, or R",
        [
            (39, 45, "programming"),
            (50, 51, "programming")
        ]
    ),
    (
        "Experience in using industry standard Java IDE such as IntelliJ is an asset.",
        [
            (38, 42, "programming")
        ]
    ),
    (
        "Advanced SQL skills, including but not limited to using subqueries, pivot/unpivot, window functions, etc.",
        [
            (9, 12, "programming")
        ]
    ),
    (
        "Prior usage of cloud computing platform such as GCP, AWS or Azure",
        [
            (48, 51, "cloud"),
            (53, 56, "cloud"),
            (60, 65, "cloud")
        ]
    )

]