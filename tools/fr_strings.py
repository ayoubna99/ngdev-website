# French translations for tools/build_fr.py.
# Keys are the English text exactly as it appears in index.html (whitespace collapsed,
# HTML entities kept as written, e.g. "&amp;").

# Text that stays the same in French (names, products, tech, code-style labels).
KEEP = {
    'NG Development', '/', 'ng.web()', 'ng.mobile()', 'ng.backend()', 'ng.servers()', 'ng.backup()',
    'ng.secure()', 'ng.support()', 'ng.deploy()', 'ng.audit()', 'Active Directory',
    'Virtualization: Hyper-V, VMware, Proxmox', 'Grant Thornton Algeria', '2MP Industrie, Blida',
    'Alrim, Oued Smar', 'Nadjem Ayoub', 'Mekhlef Mohamed Oussama', 'Laravel', 'PHP', 'Flutter', 'Kotlin',
    'TypeScript', 'Playwright', 'PostgreSQL', 'MySQL', 'Supabase', 'Docker', 'GitHub Actions',
    'OWASP Top 10', 'DAST', 'Kaspersky EDR Foundations', 'Kaspersky · 2025', 'Veeam', 'CompTIA A+',
    'CompTIA', 'Kaspersky', 'ESET', 'Sophos', 'Microsoft Defender', 'Intune', 'Microsoft 365', 'Exchange',
    'SharePoint', 'Synology', 'QNAP', 'Hyper-V', 'VMware', 'Proxmox', 'Protectiny.com', 'Flotte-360.com',
    'protectiny/dns-filtering', 'SaaS', 'Web + Mobile', 'naqli/transit-app', 'Metro (SEMA)', 'Tram (SETRAM)',
    'guess-my-grade/android', 'Android', 'ngmed/b2b-commerce', 'E-Commerce', 'Life', 'life/android',
    'Meta Global AI Hackathon', 'EN, FR, AR, DE, ES', 'COSMOS 1980', '~294 K', 'skyshift/spherex',
    'NASA Space Apps 2026', 'recon --target ██████████.dz', 'recon/restricted', 'Pentesting',
    'ngdev — zsh', 'business@ngdev.org', 'ngdev.org', '+213 772 65 34 69', '· Mekhlef M. Oussama', 'Alex',
    'alex@company.com', 'NG Development, back to top', 'Google Cybersecurity', 'Laravel REST APIs',
    'API design &amp; development', 'Backend &amp; APIs', 'Web Apps', 'Life — Screen Time &amp; Daily Planning App',
    'Interventions', 'Certifications', 'FR', 'français', 'Version française', '25 min', '30 min', '10 min',
}

TEXT = {
    # head
    'NG Development — Software &amp; IT Services for Modern Businesses':
        'NG Development — Logiciels &amp; services informatiques pour les entreprises',
    'NG Development builds web, mobile and backend software, and installs, secures and supports the infrastructure it runs on: servers, backups, cybersecurity and IT support.':
        "NG Development conçoit des logiciels web, mobiles et backend, et installe, sécurise et maintient l'infrastructure qui les fait tourner : serveurs, sauvegardes, cybersécurité et support informatique.",
    # nav
    'Main': 'Principal',
    'services': 'services', 'field': 'terrain', 'team': 'équipe', 'work': 'projets', 'about': 'à-propos',
    'process': 'méthode', 'Get in touch': 'Nous contacter', 'Open menu': 'Ouvrir le menu',
    'get-in-touch': 'contact',
    # hero
    'software-and-it-studio/': 'studio-logiciel-et-informatique/',
    'We build your software and run the systems behind it.':
        'Nous créons vos logiciels et gérons vos systèmes.',
    'NG Development designs and builds digital products, and installs, secures and supports the infrastructure they run on, from the first line of code to the server rack.':
        "NG Development conçoit et développe des produits numériques, puis installe, sécurise et maintient l'infrastructure qui les fait tourner, de la première ligne de code jusqu'à la baie serveur.",
    'Explore services': 'Nos services',
    'Started': 'Depuis', 'Projects shipped': 'Projets livrés', 'IT interventions': 'Interventions IT',
    'Client retention': 'Clients fidèles',
    # marquee
    'What we build': 'Ce que nous faisons',
    'web-application-development': 'développement-web', 'mobile-apps': 'applications-mobiles',
    'backend-systems': 'systèmes-backend', 'saas-products': 'produits-saas', 'api-development': 'développement-api',
    'cloud-infrastructure': 'infrastructure-cloud', 'servers-and-networks': 'serveurs-et-réseaux',
    'cybersecurity': 'cybersécurité', 'backup-and-recovery': 'sauvegarde-et-restauration',
    'it-support': 'support-informatique', 'security-audits': 'audits-de-sécurité',
    # statement
    'From custom apps to servers, backups and endpoint security, we build, run and protect the technology your business depends on.':
        'Des applications sur mesure aux serveurs, sauvegardes et à la sécurité des postes, nous construisons, exploitons et protégeons la technologie dont votre entreprise dépend.',
    # services
    'Everything your business runs on, under one roof': 'Tout ce qui fait tourner votre entreprise, sous un même toit',
    'From the app your customers use to the servers, backups and security behind it, one team designs it, builds it, installs it and keeps it running. No hand-offs between contractors, no gaps.':
        "De l'application utilisée par vos clients aux serveurs, sauvegardes et à la sécurité qui la soutiennent, une seule équipe conçoit, développe, installe et maintient le tout. Pas de relais entre prestataires, pas de zones grises.",
    'Web Applications': 'Applications web',
    'Full-featured web applications, showcase sites and SaaS products, designed around your users and built to hold up at scale.':
        'Applications web complètes, sites vitrines et produits SaaS, pensés pour vos utilisateurs et conçus pour tenir la charge.',
    'Custom web apps &amp; SaaS platforms': 'Applications web sur mesure &amp; plateformes SaaS',
    'Showcase websites': 'Sites vitrines', 'Online payments (Slick Pay)': 'Paiement en ligne (Slick Pay)',
    'Mobile Apps': 'Applications mobiles',
    'Cross-platform apps for iOS and Android that are fast, intuitive and built around how your users actually behave.':
        'Applications multiplateformes iOS et Android, rapides, intuitives et conçues selon les usages réels de vos utilisateurs.',
    'iOS &amp; Android (Flutter)': 'iOS &amp; Android (Flutter)', 'Native Android apps': 'Applications Android natives',
    'Google Play publishing': 'Publication sur Google Play', 'AI-powered features': "Fonctionnalités basées sur l'IA",
    'Reliable backends that power your product, built for real traffic, with security and maintainability from day one.':
        'Des backends fiables qui alimentent votre produit, prêts pour un trafic réel, avec la sécurité et la maintenabilité dès le premier jour.',
    'Data pipelines &amp; integrations': 'Pipelines de données &amp; intégrations',
    'Billing &amp; subscription systems': "Facturation &amp; systèmes d'abonnement",
    'Cloud hosting &amp; monitoring': 'Hébergement cloud &amp; supervision',
    'Servers &amp; Infrastructure': 'Serveurs &amp; infrastructure',
    'Installation, configuration and administration of your server environments, on-premises and in the cloud.':
        'Installation, configuration et administration de vos environnements serveurs, en local et dans le cloud.',
    'File sharing &amp; DHCP servers': 'Serveurs de partage &amp; DHCP',
    'High-availability services': 'Haute disponibilité des services',
    'Network &amp; infrastructure services': "Réseaux &amp; services d'infrastructure",
    'Backup &amp; Recovery': 'Sauvegarde &amp; restauration',
    "Backups only count if they restore. We set them up, schedule them, verify them and test the restore, so a bad day stays a small one.":
        "Une sauvegarde ne vaut que si elle se restaure. Nous la mettons en place, la planifions, la vérifions et testons la restauration, pour qu'un incident reste un petit incident.",
    'Local backup solutions (Veeam)': 'Solutions de sauvegarde locale (Veeam)',
    'NAS storage servers (Synology, QNAP)': 'Serveurs de stockage NAS (Synology, QNAP)',
    'Scheduling &amp; verification': 'Planification &amp; vérification', 'Restore testing': 'Tests de restauration',
    'Cybersecurity': 'Cybersécurité',
    'Protect every device and every account, with the right people having the right access, and nothing more.':
        'Protéger chaque appareil et chaque compte : les bonnes personnes ont les bons accès, et rien de plus.',
    'Endpoint protection: Kaspersky, ESET, Sophos, Defender': 'Protection des postes : Kaspersky, ESET, Sophos, Defender',
    'Access security': 'Sécurisation des accès', 'Rights &amp; permissions management': 'Gestion des droits &amp; permissions',
    'Web &amp; application filtering': 'Filtrage web &amp; applicatif', 'Firewall management': 'Gestion du pare-feu',
    'IT Support &amp; Training': 'Support &amp; formation',
    'Hands-on support for your team and your equipment, on-site or remote, plus training so your people use their tools with confidence.':
        'Un support concret pour vos équipes et votre matériel, sur site ou à distance, et des formations pour que chacun maîtrise ses outils.',
    'Level 2 / Level 3 technical support': 'Support technique N2 / N3',
    'Incident diagnosis &amp; resolution': "Diagnostic &amp; résolution d'incidents",
    'User, access &amp; internet management': 'Gestion des utilisateurs, accès &amp; internet',
    'Equipment repair &amp; fleet renewal': 'Réparation &amp; renouvellement du parc',
    'Endpoint &amp; office-tools training': 'Formation antivirus &amp; bureautique',
    'Deployment &amp; Migration': 'Déploiement &amp; migration',
    'Moving to new servers or rolling out a new solution, planned and documented so your business keeps running during the switch.':
        "Changer de serveurs ou déployer une nouvelle solution, de façon planifiée et documentée, pour que votre activité continue pendant la transition.",
    'Server rack installation': 'Installation de baies serveurs', 'Server &amp; service migration': 'Migration de serveurs &amp; services',
    'Solution deployment': 'Déploiement de solutions', 'Hosting &amp; ongoing support': 'Hébergement &amp; accompagnement',
    'Security Audits': 'Audits de sécurité',
    'We test your website the way an attacker would, using Recon, our private in-house engine, then hand you a clear, prioritized list of what to fix.':
        "Nous testons votre site comme le ferait un attaquant, avec Recon, notre moteur interne privé, puis vous remettons une liste claire et priorisée des corrections à faire.",
    'Website &amp; web app pentesting': "Pentest de sites &amp; d'applications web",
    'Exposure &amp; misconfiguration checks': "Contrôle de l'exposition &amp; des mauvaises configurations",
    'Prioritized remediation report': 'Rapport de remédiation priorisé', 'Retest after fixes': 'Nouveau test après correction',
    # field
    'in-the-field/': 'sur-le-terrain/',
    'Real interventions, real server rooms': 'De vraies interventions, de vraies salles serveurs',
    'Half of what we do happens on-site: racks, servers, security appliances, workstations and training for the teams that depend on them. A few moments from recent interventions.':
        "La moitié de notre travail se fait sur site : baies, serveurs, équipements de sécurité, postes de travail et formation des équipes qui en dépendent. Quelques moments de nos interventions récentes.",
    'Network &amp; server room, Grant Thornton Algeria': 'Salle réseau &amp; serveurs, Grant Thornton Algeria',
    'Network &amp; server room': 'Salle réseau &amp; serveurs',
    'Office-tools training session led by our team': 'Session de formation bureautique animée par notre équipe',
    'Office-tools training': 'Formation bureautique', 'On-site session': 'Session sur site',
    'Training session': 'Session de formation',
    'Rack &amp; server installation, 2MP Industrie, Blida': 'Installation de baie &amp; serveurs, 2MP Industrie, Blida',
    'Rack &amp; server installation': 'Installation de baie &amp; serveurs',
    'Security appliance maintenance, Symantec hardware': "Maintenance d'un équipement de sécurité Symantec",
    'Security appliance maintenance': "Maintenance d'un équipement de sécurité",
    'Symantec hardware': 'Matériel Symantec',
    'HP ProLiant server diagnostic, Workshop': 'Diagnostic de serveur HP ProLiant, atelier',
    'HP ProLiant server diagnostic': 'Diagnostic de serveur HP ProLiant', 'Workshop': 'Atelier',
    'Server room intervention, Alrim, Oued Smar': 'Intervention en salle serveurs, Alrim, Oued Smar',
    'Server room intervention': 'Intervention en salle serveurs',
    # team
    'co-founders/': 'co-fondateurs/',
    'Meet the people behind NG Development': "Les personnes derrière NG Development",
    'Two co-founders, two complementary skill sets: one builds the software, the other runs and protects the infrastructure it lives on. Together they cover the whole stack.':
        "Deux co-fondateurs, deux expertises complémentaires : l'un développe les logiciels, l'autre exploite et protège l'infrastructure qui les héberge. Ensemble, ils couvrent toute la chaîne.",
    'Co-founder · Software engineering &amp; security': 'Co-fondateur · Ingénierie logicielle &amp; sécurité',
    "Self-taught software engineer who was coding well before university. Leads engineering on every product, with teams of up to five engineers, and specializes in autonomous AI agents and application &amp; network security: Recon-AI, Life, NAQLI, SkyShift and Protectiny's platform.":
        "Ingénieur logiciel autodidacte, il codait bien avant l'université. Il dirige le développement de chaque produit, avec des équipes allant jusqu'à cinq ingénieurs, et s'est spécialisé dans les agents IA autonomes et la sécurité applicative &amp; réseau : Recon-AI, Life, NAQLI, SkyShift et la plateforme Protectiny.",
    'Engineers per team led': 'Ingénieurs par équipe dirigée', 'Recon-AI detection modules': 'Modules de détection Recon-AI',
    'Automated tests in Life': 'Tests automatisés dans Life', 'highlights/': 'parcours/',
    'Professional Certificate': 'Certificat professionnel', 'BSc Computer Science': 'Licence en informatique',
    'University of Ghardaia · 2026': 'Université de Ghardaïa · 2026', 'Hackathons': 'Hackathons',
    'NASA Space Apps 2026 (team lead) · Meta Global AI': "NASA Space Apps 2026 (chef d'équipe) · Meta Global AI",
    'stack/': 'outils/', 'Python (async)': 'Python (async)', 'LLM agents': 'Agents LLM',
    'Co-founder · IT infrastructure &amp; security': 'Co-fondateur · Infrastructure IT &amp; sécurité',
    'Leads infrastructure, networks and cybersecurity: more than 400 on-site and remote interventions since 2022, from server rooms and backups to endpoint protection.':
        "Responsable de l'infrastructure, des réseaux et de la cybersécurité : plus de 400 interventions sur site et à distance depuis 2022, des salles serveurs et sauvegardes à la protection des postes.",
    'In the field since': 'Sur le terrain depuis', 'certifications/': 'certifications/',
    'Technical sales': 'Technico-commercial',
    'how-we-work-on-site/': 'nos-interventions/',
    'Every intervention is scoped, adapted to your context and systematically documented, with full respect for the confidentiality and security of the information shared.':
        'Chaque intervention est cadrée, adaptée à votre contexte et systématiquement documentée, dans le respect de la confidentialité et de la sécurité des informations échangées.',
    'our-saas-products/': 'nos-produits-saas/',
    'Cybersecurity made simple for non-technical people': 'La cybersécurité simplifiée pour les non-techniciens',
    'SaaS fleet management platform': 'Plateforme SaaS de gestion de flotte',
    # work
    'selected-work/': 'réalisations/', 'Case studies': 'Études de cas', 'Start a project': 'Lancer un projet',
    'Protectiny web dashboard showing blocked DNS requests': 'Tableau de bord web Protectiny, requêtes DNS bloquées', 'Security': 'Sécurité',
    'Protectiny — DNS Filtering SaaS Platform': 'Protectiny — Plateforme SaaS de filtrage DNS',
    'problem/': 'problème/', 'solution/': 'solution/', 'result/': 'résultat/',
    'Businesses lacked an accessible, locally-adapted solution for DNS-level network security. Existing tools were either too complex for small teams or priced for enterprise budgets.':
        "Les entreprises manquaient d'une solution accessible et adaptée au marché local pour la sécurité réseau au niveau DNS. Les outils existants étaient trop complexes pour les petites équipes ou trop chers.",
    'We built a full DNS filtering platform from scratch, covering the web dashboard, mobile app, billing integrations, and device provisioning API, with an interface that makes security management straightforward for any team size.':
        "Nous avons construit de zéro une plateforme complète de filtrage DNS : tableau de bord web, application mobile, intégrations de paiement et API de provisionnement des appareils, avec une interface qui rend la sécurité simple à gérer, quelle que soit la taille de l'équipe.",
    'Launched as the first DNS filtering SaaS targeting the Algerian market. Subscription billing, device management, and real-time filtering are fully operational in production with active customers.':
        "Lancé comme le premier SaaS de filtrage DNS destiné au marché algérien. Abonnements, gestion des appareils et filtrage en temps réel sont en production avec des clients actifs.",
    'Visit protectiny.com': 'Visiter protectiny.com',
    'Public transport mobile app': 'Application mobile de transport public', 'Mobile App': 'Application mobile',
    'Transit': 'Transport',
    'NAQLI — Unified Public Transport App for Algeria': "NAQLI — L'application unifiée des transports publics en Algérie",
    'Riders in Algeria had to deal with each transport operator separately, buying tickets and managing subscriptions for the metro, tram and train in different places.':
        "En Algérie, les voyageurs devaient traiter avec chaque opérateur séparément : tickets et abonnements pour le métro, le tram et le train s'achetaient à des endroits différents.",
    'One app that covers the metro (SEMA), the tram (SETRAM) and the train (SNTF), so riders buy tickets and manage their subscriptions in a single place.':
        "Une seule application pour le métro (SEMA), le tram (SETRAM) et le train (SNTF) : les voyageurs achètent leurs tickets et gèrent leurs abonnements au même endroit.",
    'Train (SNTF)': 'Train (SNTF)', 'Ticket purchase': 'Achat de tickets', 'Subscription management': 'Gestion des abonnements',
    'Three operators, one app, built by a five-person team on Laravel and Flutter. Tickets are secured with HMAC-SHA256 signed QR codes and paid through SATIM, with an inspector role for on-site validation. The project has been submitted to the Ministry of Transport, which is currently studying it.':
        "Trois opérateurs, une application, développée par une équipe de cinq personnes avec Laravel et Flutter. Les tickets sont sécurisés par des QR codes signés HMAC-SHA256 et payés via SATIM, avec un rôle de contrôleur pour la validation sur place. Le projet a été soumis au ministère des Transports, qui l'étudie actuellement.",
    'Education mobile application': 'Application mobile éducative', 'Education': 'Éducation',
    'Guess My Grade — Academic Performance Tool': 'Guess My Grade — Outil de suivi des résultats',
    'Students had no quick way to estimate their final grades or understand what scores they needed on upcoming exams to reach their target, forcing manual, error-prone calculations.':
        "Les étudiants n'avaient aucun moyen rapide d'estimer leur moyenne ou de savoir quelles notes viser aux prochains examens, d'où des calculs manuels sources d'erreurs.",
    'A lightweight Android app allowing students to input their module scores and weighted credits, instantly calculating current averages and the minimum grades needed to reach a target GPA. Clean UI designed for quick daily use.':
        "Une application Android légère : l'étudiant saisit ses notes et coefficients, et obtient instantanément sa moyenne actuelle et les notes minimales nécessaires pour atteindre son objectif. Une interface claire, pensée pour un usage quotidien.",
    'Published on Google Play Store with positive user feedback. Students report using it before every exam session to understand exactly what they need to achieve, turning anxiety into actionable information.':
        "Publiée sur Google Play avec des retours positifs. Les étudiants l'utilisent avant chaque session d'examens pour savoir exactement ce qu'ils doivent obtenir : l'angoisse devient une information concrète.",
    'Medical equipment e-commerce platform': "Plateforme e-commerce d'équipement médical",
    'Healthcare': 'Santé', 'B2B Platform': 'Plateforme B2B', 'Shipped': 'Livré',
    'ngmed — B2B Medical Equipment Commerce Platform': "ngmed — Plateforme B2B de vente d'équipement médical",
    'Hospitals and clinics procuring medical equipment had no dedicated digital channel. Purchases happened through phone calls, paper catalogues, and manual invoicing that introduced errors, delays, and zero visibility into order status.':
        "Les hôpitaux et cliniques n'avaient aucun canal numérique dédié pour acheter du matériel médical. Tout passait par téléphone, catalogues papier et factures manuelles : erreurs, retards et aucune visibilité sur les commandes.",
    'A full B2B e-commerce platform purpose-built for the medical supply chain, covering product catalogue management, order processing, and automated invoice generation with tax calculation, all in one coherent system tailored for institutional buyers.':
        "Une plateforme e-commerce B2B complète, conçue pour la chaîne d'approvisionnement médicale : catalogue produits, traitement des commandes et facturation automatique avec calcul des taxes, dans un système cohérent adapté aux acheteurs institutionnels.",
    'Product catalogue &amp; inventory': 'Catalogue &amp; stock', 'Order management': 'Gestion des commandes',
    'Tax-aware invoicing': 'Facturation avec taxes', 'Client accounts &amp; pricing tiers': 'Comptes clients &amp; grilles tarifaires',
    'PDF invoice generation': 'Factures PDF', 'Order history &amp; tracking': 'Historique &amp; suivi des commandes',
    'Full platform built, pre-deployment phase. Targets hospitals, clinics, and medical procurement teams, replacing manual ordering workflows with a structured, auditable digital process.':
        "Plateforme complète développée, en phase de pré-déploiement. Elle cible les hôpitaux, cliniques et services achats médicaux, en remplaçant les commandes manuelles par un processus numérique structuré et traçable.",
    'of 15 min': 'sur 15 min', 'used this hour': 'utilisées cette heure', 'Tomorrow': 'Demain',
    'Finish the slides': 'Finir les slides', 'First step: open the draft': 'Première étape : ouvrir le brouillon',
    'Go for a run': 'Aller courir', 'Call the bank': 'Appeler la banque', 'Hour limit reached': 'Limite horaire atteinte',
    'Your goal: finish the slides. Next: open the draft (25&nbsp;min).':
        'Votre objectif : finir les slides. Ensuite : ouvrir le brouillon (25&nbsp;min).',
    'AI Agent': 'Agent IA', 'Open source': 'Open source', 'Coming soon on Google Play': 'Bientôt sur Google Play',
    'Life — Screen Time &amp; Daily Planning App': "Life — Temps d'écran &amp; planification quotidienne",
    'Hours disappear into endless scrolling, and generic screen-time warnings are easy to ignore because they say nothing about what you actually wanted to do instead.':
        "Les heures disparaissent dans le défilement sans fin, et les alertes génériques de temps d'écran s'ignorent facilement car elles ne disent rien de ce que vous vouliez vraiment faire.",
    "Pick the apps that eat your time and set an hourly limit of 5 to 30 minutes. Each night, type tomorrow's plan as messily as you like and Life turns it into a short task list with a first step and a time estimate. When you hit your limit, it reminds you of your own goal and next task. It never blocks your apps.":
        "Choisissez les applications qui vous prennent du temps et fixez une limite horaire de 5 à 30 minutes. Chaque soir, notez le programme du lendemain comme il vient, et Life le transforme en une courte liste de tâches avec une première étape et une estimation de durée. Quand vous atteignez la limite, il vous rappelle votre objectif et votre prochaine tâche. Il ne bloque jamais vos applications.",
    'Hourly app limits': 'Limites horaires par app', 'AI nightly planning': 'Planification IA du soir',
    'Gentle &amp; Active modes': 'Modes Doux &amp; Actif', 'Reality check': 'Bilan réaliste', '14-day progress': 'Progrès sur 14 jours',
    'No account needed': 'Sans compte', 'privacy/': 'confidentialité/',
    "App usage stays on the phone. Only the nightly plan text is sent to the server, and it is deleted right after processing. Life doesn't use Android's Accessibility service and never reads what's inside other apps.":
        "L'utilisation des applications reste sur le téléphone. Seul le texte du programme du soir est envoyé au serveur, et il est supprimé juste après traitement. Life n'utilise pas le service d'accessibilité d'Android et ne lit jamais le contenu des autres applications.",
    'View Life on GitHub': 'Voir Life sur GitHub', 'Web App': 'Application web', 'Space Data': 'Données spatiales',
    'SkyShift — See What Moved Across the Sky': "SkyShift — Voir ce qui a traversé le ciel",
    "NASA's SPHEREx telescope maps the whole sky, but finding what moved through a given patch, like asteroids or satellites streaking across the frames, means digging through raw survey images by hand.":
        "Le télescope SPHEREx de la NASA cartographie tout le ciel, mais retrouver ce qui a traversé une zone donnée, comme des astéroïdes ou des satellites, impose de fouiller à la main les images brutes.",
    "Point at any patch of sky and SkyShift shows what moved through it in SPHEREx images: stars, asteroids, and the satellites crossing the data, with each satellite's temperature estimated from SPHEREx's two cameras.":
        "Pointez n'importe quelle zone du ciel et SkyShift montre ce qui l'a traversée dans les images SPHEREx : étoiles, astéroïdes et satellites, avec la température de chaque satellite estimée grâce aux deux caméras de SPHEREx.",
    'Recovered satellite thermal signatures that the SPHEREx pipeline normally masks and discards, the first such temperature measurements from this telescope, including COSMOS 1980 at ~294 K. Built by a three-person team and shipped live during the NASA Space Apps Challenge 2026.':
        "Récupération de signatures thermiques de satellites que le pipeline SPHEREx masque et écarte habituellement : les premières mesures de température de ce type issues de ce télescope, dont COSMOS 1980 à ~294 K. Réalisé par une équipe de trois personnes et mis en ligne pendant le NASA Space Apps Challenge 2026.",
    'Open spherex.ngdev.org': 'Ouvrir spherex.ngdev.org', 'Source on GitHub': 'Code source sur GitHub',
    'recon — restricted': 'recon — accès restreint',
    '[+] mapping attack surface': "[+] cartographie de la surface d'attaque", '[+] fingerprinting stack': '[+] identification de la stack',
    '[+] probing': '[+] sondage', '[+] chaining findings': '[+] chaînage des résultats',
    '[✓] report ready → owner only': '[✓] rapport prêt → propriétaire uniquement',
    'private': 'privé', 'In-house tool': 'Outil interne', 'Private · not public': 'Privé · non public',
    'Recon-AI — AI-Assisted Website Security Scanner': 'Recon-AI — Scanner de sécurité web assisté par IA',
    'Most small businesses never have their website security-tested. Professional pentests are slow and expensive, so weaknesses sit unnoticed until someone else finds them first.':
        "La plupart des petites entreprises ne font jamais tester la sécurité de leur site. Les pentests professionnels sont lents et coûteux, et les failles restent invisibles jusqu'à ce que quelqu'un d'autre les trouve.",
    'A deterministic detection engine with 20+ modules (XSS, SQL injection, SSTI, broken access control, secrets, TLS/DNS/email) paired with an AI agent that adapts payloads to the target, confirms real exploits and re-tests every finding to cut false positives. Results come as clear, prioritized reports.':
        "Un moteur de détection déterministe de plus de 20 modules (XSS, injection SQL, SSTI, contrôle d'accès défaillant, secrets exposés, TLS/DNS/e-mail) couplé à un agent IA qui adapte les charges à la cible, confirme les failles réelles et re-teste chaque résultat pour éliminer les faux positifs. Les résultats sont livrés sous forme de rapports clairs et priorisés.",
    'why-private/': 'pourquoi-privé/',
    'Recon-AI is effective enough that releasing it would hand the same capabilities to attackers. So it stays private, for security reasons: we run it ourselves, only on sites whose owners have authorized the test, and the findings go to them alone.':
        "Recon-AI est assez efficace pour que sa publication donne les mêmes capacités aux attaquants. Il reste donc privé, pour des raisons de sécurité : nous l'utilisons nous-mêmes, uniquement sur des sites dont les propriétaires ont autorisé le test, et les résultats ne sont communiqués qu'à eux.",
    'Request a security audit': 'Demander un audit de sécurité',
    # about
    'NG Development studio summary': 'Présentation du studio NG Development',
    'about/': 'à-propos/',
    'A team focused on shipping software that actually works.': 'Une équipe qui livre des logiciels qui fonctionnent vraiment.',
    "At NG Development, we build software the way we'd want it built for ourselves: with clean architecture, thoughtful design, and a serious commitment to reliability. We work closely with our clients through every phase of a project, and we don't ship until we're confident it's ready for the real world.":
        "Chez NG Development, nous construisons les logiciels comme nous voudrions qu'on les construise pour nous : architecture propre, conception réfléchie et un vrai engagement envers la fiabilité. Nous travaillons main dans la main avec nos clients à chaque étape, et nous ne livrons que lorsque nous sommes sûrs que c'est prêt pour le monde réel.",
    "We're a lean team with broad expertise across web, mobile, and backend systems, plus IT infrastructure, networks and cybersecurity. That means faster decisions, fewer layers, and direct communication with the people doing the actual work. Our clients come back because we deliver what we commit to, and we're honest when things need to change.":
        "Nous sommes une équipe resserrée, avec une large expertise en web, mobile et backend, ainsi qu'en infrastructure IT, réseaux et cybersécurité. Résultat : des décisions plus rapides, moins d'intermédiaires et un échange direct avec ceux qui font le travail. Nos clients reviennent parce que nous tenons nos engagements, et que nous sommes francs quand quelque chose doit changer.",
    'Reliability first': "La fiabilité d'abord",
    'We build systems that hold up under real conditions, not just demos.': 'Des systèmes qui tiennent en conditions réelles, pas seulement en démo.',
    'Clean code, always': 'Un code propre, toujours',
    'Every project is built to be maintained, extended, and handed off cleanly.': 'Chaque projet est conçu pour être maintenu, étendu et transmis proprement.',
    'Honest communication': 'Une communication honnête',
    "We tell you what's realistic and flag issues before they become problems.": "Nous disons ce qui est réaliste et signalons les risques avant qu'ils ne deviennent des problèmes.",
    'Long-term thinking': 'Une vision à long terme',
    "We design for where your business is going, not just where it is today.": "Nous concevons pour là où va votre entreprise, pas seulement là où elle est aujourd'hui.",
    # process
    'how-we-work/': 'notre-méthode/',
    'A process built for predictable delivery': 'Une méthode pensée pour des livraisons prévisibles',
    "We follow a structured development process that keeps projects moving forward without surprises. Each phase has clear outputs and a defined handoff, so you always know what's happening and what comes next.":
        "Nous suivons un processus structuré qui fait avancer les projets sans mauvaises surprises. Chaque phase a des livrables clairs et une transition définie : vous savez toujours où en est le projet et ce qui vient ensuite.",
    '01_discovery': '01_découverte', 'Discovery': 'Découverte',
    "We start by understanding your business, your users, and the problem you're trying to solve, before writing a single line of code.":
        "Nous commençons par comprendre votre activité, vos utilisateurs et le problème à résoudre, avant d'écrire la moindre ligne de code.",
    '02_planning': '02_planification', 'Planning': 'Planification',
    "Architecture decisions, scope definition, and a clear roadmap. We align on what's being built and how, so there are no surprises mid-project.":
        "Choix d'architecture, périmètre et feuille de route claire. Nous nous accordons sur ce qui sera construit et comment, pour éviter les surprises en cours de projet.",
    '03_development': '03_développement', 'Development': 'Développement',
    'Iterative development with regular check-ins. We build in focused cycles, share progress frequently, and adapt quickly to feedback.':
        "Un développement itératif avec des points réguliers. Nous avançons par cycles ciblés, partageons souvent l'avancement et intégrons vite vos retours.",
    '04_testing': '04_tests', 'Testing': 'Tests',
    "Thorough testing across devices, edge cases, and real-world scenarios. We don't consider something done until it behaves correctly under pressure.":
        "Des tests approfondis sur différents appareils, cas limites et scénarios réels. Rien n'est terminé tant que ça ne fonctionne pas correctement sous pression.",
    '05_deployment': '05_déploiement', 'Deployment': 'Déploiement',
    'Smooth, stable releases with proper infrastructure setup, monitoring, and post-launch support to make sure everything runs as expected.':
        "Des mises en production fluides et stables, avec une infrastructure bien configurée, de la supervision et un suivi après lancement pour que tout fonctionne comme prévu.",
    # contact
    'get-in-touch/': 'contact/',
    "Let's build your next project.": 'Construisons votre prochain projet.',
    "Tell us what you're working on. We'll set up a short call to understand your needs and figure out if we're the right fit.":
        "Parlez-nous de votre projet. Nous organiserons un court appel pour comprendre vos besoins et voir si nous sommes la bonne équipe.",
    'First name': 'Prénom', 'Last name': 'Nom', 'Johnson': 'Benali', 'Email address': 'Adresse e-mail',
    'Company': 'Entreprise', 'Your company name': 'Nom de votre entreprise',
    'What are you looking for?': 'Que recherchez-vous ?', 'Select a service': 'Choisissez un service',
    'Web Application Development': "Développement d'applications web",
    'Mobile App Development': "Développement d'applications mobiles",
    'Backend &amp; System Development': 'Développement backend &amp; systèmes',
    'Servers &amp; IT Infrastructure': 'Serveurs &amp; infrastructure IT',
    'IT Support': 'Support informatique', 'Website Security Audit': 'Audit de sécurité de site web',
    'Full Product Build': 'Développement de produit complet', 'Something else': 'Autre chose',
    'Tell us about your project': 'Parlez-nous de votre projet',
    "Briefly describe what you're building, the problem you're solving, and your timeline if you have one.":
        "Décrivez brièvement votre projet, le problème à résoudre et vos délais si vous en avez.",
    'Send message': 'Envoyer le message',
    # footer
    'Software, IT &amp; security, under one roof.': 'Logiciels, informatique &amp; sécurité, sous un même toit.',
    'services/': 'services/', 'team/': 'équipe/', 'work/': 'projets/', 'contact/': 'contact/',
    'NG Development. All rights reserved.': 'NG Development. Tous droits réservés.',
    'Back to top': 'Retour en haut',
    'field/': 'terrain/', 'process/': 'méthode/',
    # section headings (the slash is a separate <span>)
    'in-the-field': 'sur-le-terrain', 'co-founders': 'co-fondateurs', 'selected-work': 'réalisations',
    'how-we-work': 'notre-méthode',
}

# Replacements inside the main <script> block (exact source text).
JS = [
    ("['v', 'software + it infrastructure']", "['v', 'logiciel + infrastructure it']"),
    ("['v', '12+ projects']", "['v', '12+ projets']"),
    ("open ? 'Close menu' : 'Open menu'", "open ? 'Fermer le menu' : 'Ouvrir le menu'"),
    ("submitLabel.textContent = 'Sending...';", "submitLabel.textContent = 'Envoi...';"),
    ("\"Thanks, we'll be in touch shortly.\"", "\"Merci, nous vous recontactons très vite.\""),
    ("submitLabel.textContent = 'Send message';", "submitLabel.textContent = 'Envoyer le message';"),
    ("'Something went wrong. Please try again or email us directly.'",
     "'Une erreur est survenue. Réessayez ou écrivez-nous directement.'"),
    ("'Network error. Please try again or email business@ngdev.org directly.'",
     "'Erreur réseau. Réessayez ou écrivez directement à business@ngdev.org.'"),
]

TEXT.update({
    'Founded NG Development': 'Fondation de NG Development',
    'Products shipped to production': 'Produits mis en production',
    'Engineers led on a single build': 'Ingénieurs dirigés sur un même projet',
    'NASA Space Apps Challenge': 'NASA Space Apps Challenge',
    'Certificate · 2026': 'Certificat · 2026',
    'Detection modules': 'Modules de détection',
    'Automated tests': 'Tests automatisés',
    'Verdicts per finding: confirmed, false positive, inconclusive': 'Verdicts par résultat : confirmé, faux positif, non concluant',
    'Automated tests (backend, Flutter, Kotlin)': 'Tests automatisés (backend, Flutter, Kotlin)',
    'Tools in the planning agent': "Outils dans l'agent de planification",
    'Token context read every night': 'Tokens de contexte analysés chaque nuit',
})

TEXT.update({
    'ai-agents': 'agents-ia',
    'AI Agents &amp; Automation': 'Agents IA &amp; automatisation',
    'Autonomous agents that plan, call tools and act on their own, with code that checks every decision against real results instead of trusting the model.':
        "Des agents autonomes qui planifient, utilisent des outils et agissent seuls, avec du code qui vérifie chaque décision sur des résultats réels au lieu de faire confiance au modèle.",
    'LLM tool calling &amp; agent loops': "Appels d'outils LLM &amp; boucles d'agents",
    'Self-learning loops (Thompson sampling)': "Boucles d'auto-apprentissage (Thompson sampling)",
    'Voice, document &amp; PDF processing': 'Traitement de la voix, des documents &amp; PDF',
    'Multi-provider LLM integration': 'Intégration LLM multi-fournisseurs',
    'Payments: SATIM, PayPal, Slick Pay': 'Paiements : SATIM, PayPal, Slick Pay',
    'Installation, administration and migration of your server environments, on-premises and in the cloud, documented so your business keeps running during the switch.':
        "Installation, administration et migration de vos environnements serveurs, en local et dans le cloud, de façon documentée pour que votre activité continue pendant la transition.",
    'Active Directory, file sharing &amp; DHCP': 'Active Directory, partage de fichiers &amp; DHCP',
    'We test your website the way an attacker would, using Recon-AI, our private in-house engine, then hand you a clear, prioritized list of what to fix.':
        "Nous testons votre site comme le ferait un attaquant, avec Recon-AI, notre moteur interne privé, puis vous remettons une liste claire et priorisée des corrections à faire.",
    'OWASP Top 10 checks': 'Contrôles OWASP Top 10',
    'Native Android (Kotlin)': 'Android natif (Kotlin)',
    'Online payments (Slick Pay, PayPal)': 'Paiement en ligne (Slick Pay, PayPal)',
    'Meet our co-founders': 'Nos co-fondateurs',
    'NG Development brings together developers, engineers and IT specialists working across software, infrastructure and security. These are the co-founders who lead the team.':
        "NG Development réunit des développeurs, des ingénieurs et des spécialistes IT qui travaillent sur le logiciel, l'infrastructure et la sécurité. Voici les co-fondateurs qui dirigent l'équipe.",
    'Co-founder · Head of Engineering': "Co-fondateur · Directeur de l'ingénierie",
    "Software engineer specialized in backend systems, autonomous AI agents and application security. Leads engineering across our products, from NAQLI's ticketing platform and the Life agent to Recon-AI, our private security scanner.":
        "Ingénieur logiciel spécialisé dans les systèmes backend, les agents IA autonomes et la sécurité applicative. Il dirige le développement de nos produits, de la plateforme de billetterie NAQLI et de l'agent Life à Recon-AI, notre scanner de sécurité privé.",
    'Co-founder · Head of IT &amp; Security': 'Co-fondateur · Directeur IT &amp; sécurité',
    'Systems, network and security engineer with more than 400 on-site and remote interventions for businesses, schools and hospitals. Leads our infrastructure, cybersecurity, backup and IT support work.':
        "Ingénieur systèmes, réseaux et sécurité, avec plus de 400 interventions sur site et à distance pour des entreprises, des écoles et des hôpitaux. Il dirige nos activités d'infrastructure, de cybersécurité, de sauvegarde et de support informatique.",
    'We built a full DNS filtering platform from scratch, covering the web dashboard, mobile app, SATIM and PayPal payments, and device provisioning API, with an interface that makes security management straightforward for any team size.':
        "Nous avons construit de zéro une plateforme complète de filtrage DNS : tableau de bord web, application mobile, paiements SATIM et PayPal et API de provisionnement des appareils, avec une interface qui rend la sécurité simple à gérer, quelle que soit la taille de l'équipe.",
    'View the NAQLI project': 'Voir le projet NAQLI',
    'Get it on Google Play': 'Disponible sur Google Play',
    'Life — An Autonomous Agent Against Doomscrolling': 'Life — Un agent autonome contre le doomscrolling',
    'Screen-time apps count your minutes and block apps, but they never ask why you picked up the phone. Their warnings are easy to ignore, and nothing learns what actually works on you.':
        "Les applications de temps d'écran comptent vos minutes et bloquent des apps, mais ne se demandent jamais pourquoi vous avez pris votre téléphone. Leurs alertes s'ignorent facilement, et rien n'apprend ce qui fonctionne vraiment sur vous.",
    "Lify, the agent inside Life, runs a closed loop on Android with no prompting: it watches real usage, slides a personal card over the app you're stuck in at the right moment, and measures whether you actually left. Every night, Meta's Muse Spark Open reads your history and proposes theories about what works on you, and code verifies them against your real results, so the model never grades itself.":
        "Lify, l'agent de Life, fonctionne en boucle fermée sur Android, sans aucune sollicitation : il observe l'utilisation réelle, affiche au bon moment une carte personnelle par-dessus l'application où vous êtes bloqué, et mesure si vous l'avez vraiment quittée. Chaque nuit, Muse Spark Open de Meta lit votre historique et propose des théories sur ce qui fonctionne pour vous, puis le code les vérifie sur vos résultats réels : le modèle ne s'évalue jamais lui-même.",
    'Contextual Thompson sampling': 'Thompson sampling contextuel',
    '3-level hierarchical priors': 'Priors hiérarchiques à 3 niveaux',
    'Nightly self-improvement': 'Auto-amélioration chaque nuit',
    'Off-policy evaluation': 'Évaluation off-policy',
    '18-tool planning agent': 'Agent de planification à 18 outils',
    'Voice &amp; PDF planning': 'Planification par la voix &amp; PDF',
    'Of nudges led to leaving the app, measured on a real phone': "Des rappels ont mené à quitter l'app, mesuré sur un vrai téléphone",
    'Vs a fixed app, on 300 simulated people (43% vs 34%)': 'Face à une app fixe, sur 300 personnes simulées (43 % contre 34 %)',
    'Life only sees which app is in front and for how long, never what you watch, your messages, location or contacts. Accounts are anonymous: no email, no phone number.':
        "Life voit seulement quelle application est ouverte et pendant combien de temps, jamais ce que vous regardez, vos messages, votre position ou vos contacts. Les comptes sont anonymes : ni e-mail, ni numéro de téléphone.",
    'Watch the 3-min demo': 'Voir la démo (3 min)',
    'Engineers first. Built for production.': "L'ingénierie d'abord. Pensé pour la production.",
    'NG Development is a software and IT company based in Algeria. We design, build and run production systems: Laravel backends and REST APIs, Flutter and Kotlin apps, autonomous AI agents, and the servers, networks and security they depend on.':
        "NG Development est une entreprise de logiciels et de services informatiques basée en Algérie. Nous concevons, développons et exploitons des systèmes en production : backends Laravel et API REST, applications Flutter et Kotlin, agents IA autonomes, ainsi que les serveurs, réseaux et la sécurité dont ils dépendent.",
    'Our work ships to real users: a DNS-security SaaS with live SATIM and PayPal payments, a transit ticketing platform now under study by the Ministry of Transport, and an AI-assisted security scanner we run on authorized audits. Every release is checked against the OWASP Top 10, tested automatically in CI and deployed with zero-downtime updates.':
        "Notre travail est utilisé par de vrais utilisateurs : un SaaS de sécurité DNS avec paiements SATIM et PayPal en production, une plateforme de billetterie de transport à l'étude au ministère des Transports, et un scanner de sécurité assisté par IA que nous utilisons lors d'audits autorisés. Chaque version est vérifiée selon l'OWASP Top 10, testée automatiquement en CI et déployée sans interruption de service.",
    'Security by default': 'La sécurité par défaut',
    'Every release is checked against the OWASP Top 10 before it ships.': "Chaque version est vérifiée selon l'OWASP Top 10 avant sa mise en ligne.",
    'Tested, not hoped': 'Testé, pas espéré',
    'Automated test suites run in CI on every product we build.': 'Des tests automatisés tournent en CI sur chacun de nos produits.',
    'AI that proves itself': "Une IA qui fait ses preuves",
    'Our agents are measured against real outcomes, never graded by the model itself.': "Nos agents sont mesurés sur des résultats réels, jamais évalués par le modèle lui-même.",
    'NAQLI home screen with quick actions': "Écran d'accueil NAQLI avec les actions rapides",
    'NAQLI metro subscription QR code': "QR code d'abonnement métro NAQLI",
    'Guess My Grade in dark mode': 'Guess My Grade en mode sombre',
    'Guess My Grade in light mode': 'Guess My Grade en mode clair',
    'Invoice generated by the ngmed platform, client details hidden': 'Facture générée par la plateforme ngmed, informations client masquées',
    'Lify explaining its updated strategy in chat': 'Lify explique sa nouvelle stratégie dans le chat',
    'Life showing what works on you and the Talk to Lify panel': 'Life montre ce qui fonctionne pour vous et le panneau Parler à Lify',
})
KEEP.update({'ng.agents()', 'LinkedIn', '+9 pts', 'Flutter + Kotlin + Supabase'})

TEXT.update({
    'Co-founder · Lead Engineer': 'Co-fondateur · Ingénieur principal',
    "Lead engineer behind our products, specialized in backend systems, autonomous AI agents and application security. From NAQLI's ticketing platform and the Life agent to Protectiny and Recon-AI, our private security scanner: ideas turned into software that holds up in production.":
        "Ingénieur principal derrière nos produits, spécialisé dans les systèmes backend, les agents IA autonomes et la sécurité applicative. De la billetterie NAQLI et de l'agent Life à Protectiny et Recon-AI, notre scanner de sécurité privé : des idées transformées en logiciels qui tiennent en production.",
    'AI agents': 'Agents IA', 'Application security': 'Sécurité applicative', 'Mobile': 'Mobile',
    'Co-founder · Head of Business Development': 'Co-fondateur · Directeur du développement commercial',
    'Leads business development, partnerships and client relationships, the first person our clients meet. A systems and network engineer with more than 400 on-site and remote interventions for businesses, schools and hospitals, he also leads our infrastructure, backup and IT support work.':
        "Il dirige le développement commercial, les partenariats et la relation client : c'est la première personne que nos clients rencontrent. Ingénieur systèmes et réseaux fort de plus de 400 interventions sur site et à distance pour des entreprises, des écoles et des hôpitaux, il pilote aussi nos activités d'infrastructure, de sauvegarde et de support informatique.",
    'Business development': 'Développement commercial', 'Partnerships': 'Partenariats',
    'Client relations': 'Relation client', 'IT infrastructure': 'Infrastructure IT',
    'all': 'tout', 'software': 'logiciel', 'ai': 'ia', 'security': 'sécurité', 'servers-&amp;-it': 'serveurs-&amp;-it',
    'IT Infrastructure': 'Infrastructure IT', 'Servers': 'Serveurs', 'On-site': 'Sur site',
    'Server Rooms &amp; Rack Installations — On-site Infrastructure': 'Salles serveurs &amp; installation de baies — Infrastructure sur site',
    'Many businesses run on server rooms that grew without a plan: tangled cabling, undocumented equipment, aging servers and backups nobody has tested.':
        "Beaucoup d'entreprises fonctionnent avec des salles serveurs qui ont grandi sans plan : câblage emmêlé, équipements non documentés, serveurs vieillissants et sauvegardes jamais testées.",
    'Our IT team installs racks and servers, sets up virtualization, Active Directory and file sharing, puts backups in place and documents everything, on-site or remotely, then stays on for support.':
        "Notre équipe IT installe les baies et les serveurs, met en place la virtualisation, Active Directory et le partage de fichiers, configure les sauvegardes et documente tout, sur site ou à distance, puis reste présente pour le support.",
    'Rack installation': 'Installation de baies', 'Server setup &amp; virtualization': 'Mise en place de serveurs &amp; virtualisation',
    'Network cabling': 'Câblage réseau', 'Backups (Veeam, NAS)': 'Sauvegardes (Veeam, NAS)',
    'Hardware diagnostics': 'Diagnostic matériel', 'Documentation': 'Documentation',
    'More than 400 on-site and remote interventions for businesses, schools and hospitals, including Grant Thornton Algeria and 2MP Industrie in Blida.':
        "Plus de 400 interventions sur site et à distance pour des entreprises, des écoles et des hôpitaux, dont Grant Thornton Algeria et 2MP Industrie à Blida.",
    'Plan a server setup': 'Planifier une installation serveur', 'See us in the field': 'Nous voir sur le terrain',
    'Filter case studies': 'Filtrer les études de cas',
    'Network and server room at Grant Thornton Algeria': 'Salle réseau et serveurs chez Grant Thornton Algeria',
    'Rack and server installation at 2MP Industrie, Blida': 'Installation de baie et de serveurs chez 2MP Industrie, Blida',
    '· replies fast': '· réponse rapide',
    'Chat with us on WhatsApp': 'Discutez avec nous sur WhatsApp', 'Chat on WhatsApp': 'Écrire sur WhatsApp',
})
KEEP.update({'Protectiny', 'it/server-rooms', 'WhatsApp'})
JS.append(("text=Hello%20NG%20Development%2C%20I%27d%20like%20to%20talk%20about%20a%20project.",
           "text=Bonjour%20NG%20Development%2C%20j%27aimerais%20parler%20d%27un%20projet."))

TEXT.update({
    'Servers &amp; Virtualization': 'Serveurs &amp; virtualisation',
    'Virtualization (Hyper-V / VMware / Proxmox)': 'Virtualisation (Hyper-V / VMware / Proxmox)',
    'File server': 'Serveur de partage', 'DHCP server': 'Serveur DHCP',
    'High availability of services': 'Haute disponibilité des services',
    'Backup &amp; Storage': 'Sauvegarde &amp; stockage',
    'Network storage servers (NAS: Synology, QNAP)': 'Serveurs de stockage réseau (NAS : Synology, QNAP)',
    'Networks &amp; Cabling': 'Réseaux &amp; câblage',
    'The network everything else depends on: switching, routing, fiber and cabling, installed cleanly and labeled so it stays maintainable.':
        "Le réseau dont tout le reste dépend : commutation, routage, fibre et câblage, installés proprement et étiquetés pour rester maintenables.",
    'Switching &amp; routing (Cisco, Huawei, Aruba)': 'Commutation &amp; routage (Cisco, Huawei, Aruba)',
    'Structured cabling &amp; fiber patching': 'Câblage structuré &amp; brassage fibre',
    'Firewalls &amp; secure internet access': 'Pare-feu &amp; accès internet sécurisé',
    'Network &amp; server room layout': 'Aménagement réseau &amp; salle serveurs',
    'Showcase sites, custom web applications and SaaS products, designed around your users and built to hold up at scale.':
        'Sites vitrines, applications web sur mesure et produits SaaS, pensés pour vos utilisateurs et conçus pour tenir la charge.',
    'Custom development': 'Développement sur mesure', 'Payment integration (Slick Pay, PayPal)': 'Intégration de paiement (Slick Pay, PayPal)',
    'SaaS platforms': 'Plateformes SaaS',
    'Microsoft 365 &amp; Workplace': 'Microsoft 365 &amp; poste de travail',
    'Email, files and devices for your whole team: Microsoft 365 set up properly, devices enrolled and protected, and workstations ready on day one.':
        "E-mails, fichiers et appareils pour toute votre équipe : Microsoft 365 bien configuré, appareils enrôlés et protégés, et postes de travail prêts dès le premier jour.",
    'Microsoft 365, Exchange &amp; SharePoint': 'Microsoft 365, Exchange &amp; SharePoint',
    'Device management (Intune)': 'Gestion des appareils (Intune)', 'Workstation rollout': 'Déploiement de postes de travail',
    'Hardware fleet renewal': 'Renouvellement du parc', 'Equipment repair': 'Réparation des équipements',
    'User &amp; internet access management': 'Gestion des utilisateurs et accès internet',
    'Server cabinet installation': 'Installation des armoires serveurs',
    'certified-team/': 'équipe-certifiée/', 'we-work-with/': 'nos-technologies/',
    'Half of what we do happens on-site: 400+ interventions across server rooms, data centers, networks, backups and workstations for businesses, schools, hospitals and public institutions.':
        "La moitié de notre travail se fait sur site : plus de 400 interventions dans des salles serveurs, data centers, réseaux, sauvegardes et postes de travail pour des entreprises, des écoles, des hôpitaux et des institutions publiques.",
    'how-we-intervene/': 'notre-façon-d-intervenir/',
    'servers': 'serveurs', 'storage-&amp;-backup': 'stockage-&amp;-sauvegarde', 'networks': 'réseaux',
    'deployment': 'déploiement', 'workplace': 'postes-de-travail', 'training': 'formation',
    'Data center intervention': 'Intervention en data center',
    'EPTV, Algerian public television': 'EPTV, télévision publique algérienne',
    'HPE ProLiant server in a production rack': 'Serveur HPE ProLiant dans une baie de production',
    'Synology RackStation &amp; NAS drives': 'Synology RackStation &amp; disques NAS',
    'Backup &amp; storage': 'Sauvegarde &amp; stockage',
    'Sophos firewall appliances': 'Pare-feu Sophos',
    'Fiber patching &amp; Cisco switching': 'Brassage fibre &amp; commutation Cisco',
    'Networks': 'Réseaux', 'Cisco 4300 series router': 'Routeur Cisco série 4300',
    'QNAP NAS in a rack': 'NAS QNAP en baie',
    'Server upgrade: memory &amp; components': 'Mise à niveau serveur : mémoire &amp; composants',
    'Huawei CloudEngine switch': 'Switch Huawei CloudEngine', 'Office workstations rollout': 'Déploiement des postes de bureau',
    'Workplace': 'Postes de travail', '12-bay NAS setup': 'Installation d’un NAS 12 baies',
    'Structured cabling': 'Câblage structuré', 'Tower server deployment': "Déploiement d'un serveur tour",
    'Rack build: switching, NAS &amp; server': 'Montage de baie : switch, NAS &amp; serveur',
    'Laptop fleet setup': "Préparation d'un parc d'ordinateurs portables", 'Workstation deployment': 'Déploiement de postes de travail',
    'HPE ProLiant first boot': 'Premier démarrage HPE ProLiant', 'Synology NAS installation': "Installation d'un NAS Synology",
    'Show all 25 photos': 'Voir les 25 photos', 'Photos from our interventions': 'Photos de nos interventions',
    'Filter photos': 'Filtrer les photos',
})
KEEP.update({'ng.network()', 'ng.workplace()', 'Cisco', 'Huawei', 'Aruba', 'Python'})
