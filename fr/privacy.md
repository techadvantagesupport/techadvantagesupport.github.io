---
layout: default
title: Politique de confidentialité BudgeTrak
lang: fr
---

<p align="right"><a href="/privacy"><b>English</b></a> · <a href="/es/privacy"><b>Español</b></a> · <a href="/de/privacy"><b>Deutsch</b></a></p>

# Politique de confidentialité BudgeTrak

**Date d'entrée en vigueur :** 11 avril 2026
**Dernière mise à jour :** 20 mai 2026

> **Remarque :** Ceci est une traduction française de courtoisie. En cas de divergence entre les versions, la [version originale en anglais](/privacy) prévaut.

## Résumé en langage clair

BudgeTrak est une application de budget personnel. Vos données financières résident sur votre appareil. Si vous choisissez d'activer la fonction SYNC pour partager votre budget entre plusieurs appareils de votre foyer, ces données sont chiffrées de bout en bout avant de quitter votre appareil — ni nous ni aucun fournisseur de cloud ne pouvons lire vos transactions, vos soldes ou les noms des commerçants. Si vous optez pour l'assistant de Chat d'aide intégré à l'application, le texte que vous y saisissez est envoyé à notre fournisseur de service d'IA pour générer des réponses et est stocké **de façon anonyme** sur nos serveurs pendant 7 jours au maximum à des fins de contrôle qualité (sans être lié à votre identité). Vos données financières ne sont jamais partagées avec des annonceurs ni utilisées pour vous profiler. Le niveau gratuit est financé par des publicités de Google AdMob, qui utilise l'identifiant publicitaire de votre appareil pour afficher des publicités personnalisées (réinitialisable dans les paramètres de votre appareil ; les publicités sont entièrement supprimées si vous passez à un niveau payant ou vous abonnez). La politique complète ci-dessous explique exactement ce qui est collecté, où cela va et comment le supprimer.

## Qui nous sommes

BudgeTrak est publiée par **Tech Advantage LLC** (« nous », « notre », « nos »). Vous pouvez nous contacter à l'adresse **support@techadvantageapps.com** pour toute question ou demande relative à la confidentialité.

## Informations que nous collectons

Nous essayons de collecter le moins possible, et nous en conservons la majeure partie uniquement sur votre appareil.

### Données sur l'appareil (toujours locales)

Lorsque vous utilisez BudgeTrak, les informations suivantes sont stockées sur votre appareil dans le stockage privé de l'application :

- **Transactions** que vous enregistrez : montant, date, nom du commerçant ou de la source, description, catégorie et toute note que vous ajoutez.
- **Configuration du budget** : vos sources de revenus, vos dépenses récurrentes, vos objectifs d'épargne, vos entrées d'amortissement et la période budgétaire que vous avez choisie (quotidienne, hebdomadaire ou mensuelle).
- **Paramètres de l'application** : symbole monétaire, format de date, thème, préférence de langue et autres choix d'affichage similaires.
- **Photos de reçus** que vous choisissez de joindre à une transaction (facultatif).
- **Fichiers de sauvegarde automatique** stockés à un emplacement de votre appareil que vous choisissez.

Ces données ne quittent jamais votre appareil à moins que vous n'activiez explicitement une fonction qui les envoie ailleurs (décrites ci-dessous). Si vous désinstallez BudgeTrak, toutes les données présentes sur l'appareil sont automatiquement supprimées par Android.

### Données de synchronisation dans le cloud (uniquement si vous y consentez)

BudgeTrak inclut une fonction facultative appelée **SYNC** qui vous permet de partager un budget familial unique entre cinq appareils au maximum. SYNC est **désactivée par défaut** et ne s'active que si vous créez explicitement un groupe SYNC ou rejoignez un groupe existant.

Si vous activez SYNC, voici ce qui se passe :

- Une clé de chiffrement est générée sur votre appareil lorsque vous créez un groupe, ou partagée de façon sécurisée via un code d'appairage de 6 caractères lorsque vous en rejoignez un.
- Vos transactions, sources de revenus, dépenses récurrentes, objectifs d'épargne, entrées d'amortissement, paramètres d'application et photos de reçus sont chiffrés **sur votre appareil** à l'aide du chiffrement ChaCha20-Poly1305 avec cette clé.
- Seules les données chiffrées sont téléversées vers notre fournisseur d'infrastructure cloud pour être relayées vers les autres appareils de votre groupe.
- La clé de chiffrement ne quitte jamais vos appareils. Notre fournisseur d'infrastructure cloud, nos serveurs et tout tiers ayant accès au stockage cloud **ne peuvent pas** déchiffrer vos données financières — ils ne voient que des blocs chiffrés.
- Chaque appareil lié déchiffre les données localement à l'aide de la clé partagée.

Lorsque vous quittez un groupe SYNC ou le dissolvez, vos données locales sont conservées sur votre appareil, mais la copie dans le cloud est supprimée (avec une fenêtre de nettoyage de 90 jours pour les données orphelines).

### Données de diagnostic et de plantage

Pour maintenir BudgeTrak stable et identifier les bogues, nous utilisons des services anonymes de **rapport de plantages** et de **télémétrie d'utilisation** fournis par notre fournisseur d'infrastructure cloud. Les deux sont **activés par défaut** et partagent une seule option de désactivation dans **Paramètres → Confidentialité → Envoyer les rapports de plantage et les données d'utilisation anonymes**. Décocher cette case les arrête tous les deux immédiatement.

Lorsque cette collecte est activée, les données que nous recueillons incluent :

- Les traces de pile de plantage et les messages d'erreur.
- Des informations anonymes sur l'appareil (modèle, version du système d'exploitation, version de l'application).
- Un identifiant utilisateur anonyme d'authentification backend — présent uniquement si vous avez utilisé une fonction qui nécessite une authentification backend (SYNC, Chat d'aide, Numérisation de reçus par IA, Catégorisation CSV par IA, ou un achat payant). Un identifiant aléatoire généré à la première utilisation, et non votre nom ou votre adresse e-mail. Les utilisateurs qui n'utilisent jamais aucune de ces fonctions ne reçoivent jamais d'identifiant utilisateur backend.
- Des compteurs de diagnostic : le nombre de transactions, de dépenses récurrentes et d'entrées de grand livre de période dont vous disposez ; l'état de synchronisation (`healthy`, `dead` ou `off`) ; le nombre d'appareils dans votre groupe SYNC ; et la date de votre dernier renouvellement de période.
- Un **condensé à sens unique (hash)** de votre solde d'Argent disponible (calculé localement sous forme de condensé hexadécimal avant d'être envoyé). La valeur réelle de l'argent ne quitte jamais votre appareil, et le hash ne peut pas être inversé pour récupérer le nombre d'origine.
- Des événements de cycle de vie horodatés tels que « écouteur démarré », « jeton renouvelé » ou « limite de période franchie », utilisés pour déboguer les problèmes de synchronisation.
- Deux événements d'utilisation anonymes : **`ocr_feedback`** enregistre si vous avez modifié le commerçant, la date ou le montant d'une transaction renseignée par la numérisation de reçus par IA (uniquement des écarts et des valeurs booléennes — jamais les valeurs elles-mêmes), et **`health_beacon`** enregistre une fois par jour si votre écouteur SYNC est connecté ainsi que le *nombre* d'enregistrements sur votre appareil.
- Des événements de démarrage analytiques standard (`first_open`, `session_start`, `app_update`) indiquant que l'application a été utilisée, mais aucune information sur *ce que* vous y avez fait.

Les données de plantage et de télémétrie **n'incluent pas** le contenu de vos transactions, les noms des commerçants, les montants, les dates, les descriptions, les catégories, les photos de reçus, les clés de chiffrement ni aucune autre information financière personnelle. Nous appliquons un hash à la seule donnée financière qui touche les diagnostics (votre solde d'argent) afin que même nous ne puissions pas la lire. Nous avons également désactivé la dérivation pays/région par IP dans notre configuration analytique, de sorte qu'aucune localisation approximative n'est collectée.

Si vous désactivez les rapports de diagnostic, rien de ce qui précède n'est collecté — le battement quotidien utilisé pour confirmer que les appareils sont en bon état et les événements de précision OCR utilisés pour améliorer la numérisation de reçus sont tous deux ignorés. Nous vous recommandons de le laisser activé afin que nous puissions détecter et corriger les bogues qui affectent les utilisateurs réels, mais le choix vous appartient.

### Authentification et lutte contre les abus

BudgeTrak vous connecte à notre backend au moyen d'une **authentification anonyme** (aucun e-mail ni mot de passe requis) uniquement lorsque vous utilisez pour la première fois une fonction qui le nécessite : **SYNC** (rejoindre ou créer un groupe de synchronisation familial), **Chat d'aide** (envoyer un message à l'assistant IA), **Numérisation de reçus par IA**, **Catégorisation CSV par IA**, ou la finalisation d'un **achat ou abonnement payant**. Tant que vous n'utilisez pas l'une de ces fonctions, votre appareil n'a aucun identifiant utilisateur backend — l'application fonctionne entièrement sur l'appareil, sans session authentifiée. La première fois que vous en utilisez une, un jeton anonyme aléatoire est généré, persiste pendant toute la durée de vie de cette installation et n'est utilisé que pour satisfaire l'exigence d'authentification de notre serveur pour la fonction correspondante. Votre appareil est également vérifié à l'aide de l'attestation d'intégrité d'application de la plateforme Android afin d'empêcher les clients non autorisés d'accéder au relais cloud. Aucun de ces systèmes ne collecte d'informations personnelles vous concernant.

### Données d'abonnement et d'achat

Si vous passez à un niveau payant ou que vous vous abonnez à BudgeTrak Premium, l'achat est traité entièrement par **Google Play Billing** (le système standard d'achats intégrés d'Android). Nous ne voyons pas votre moyen de paiement, votre numéro de carte bancaire ni votre adresse de facturation — Google Play gère tout cela. Nous recevons uniquement une confirmation de la validité de votre achat, utilisée pour déverrouiller les fonctions correspondantes dans l'application.

### Publicité (niveau gratuit uniquement)

Le niveau gratuit de BudgeTrak affiche des publicités natives diffusées via un réseau publicitaire. Le réseau peut collecter un identifiant publicitaire Android limité et des informations de base sur l'appareil pour diffuser des publicités. Vous pouvez réinitialiser ou limiter votre **identifiant publicitaire Android** dans les paramètres de votre appareil à tout moment. Si vous passez à un niveau payant ou que vous vous abonnez à Premium, les publicités sont entièrement supprimées.

### Ce que nous ne collectons **pas**

Nous tenons à être précis sur ce point. BudgeTrak **ne collecte pas** :

- Votre nom, votre adresse e-mail, votre numéro de téléphone ni aucune autre information personnelle directement identifiante.
- Votre emplacement physique, vos coordonnées GPS ou votre adresse IP (au-delà de ce que les services de la plateforme reçoivent automatiquement pour le routage).
- Vos contacts, votre calendrier, votre photothèque (autres que les photos de reçus que vous joignez explicitement), votre historique d'appels, vos messages SMS ou votre historique de navigation.
- Les identifiants de votre compte bancaire, vos numéros d'acheminement ou vos informations de connexion à un quelconque établissement financier.
- Toute donnée de santé, de forme physique ou biométrique.

## Comment nous utilisons les informations

Nous utilisons les informations limitées que nous collectons exclusivement aux fins suivantes, et rien d'autre :

- **Pour fournir les fonctionnalités essentielles de l'application** (calculer votre budget, synchroniser les données entre vos appareils si vous y avez consenti, afficher vos transactions).
- **Pour diagnostiquer les plantages et les bogues** afin de les corriger dans la prochaine version.
- **Pour vérifier l'intégrité de votre abonnement** si vous avez effectué une mise à niveau.
- **Pour diffuser des publicités** sur le niveau gratuit via notre réseau publicitaire.

Nous **ne** :

- Vendons vos données à qui que ce soit, jamais, pour quelque raison que ce soit.
- Partageons vos données avec des courtiers en données, des réseaux de marketing ou des sociétés d'analyse (au-delà des sous-traitants tiers énumérés ci-dessous).
- Utilisons vos données financières pour entraîner des modèles d'apprentissage automatique ou des systèmes d'IA.
- Utilisons vos données financières à des fins publicitaires ni pour établir un profil de vous.

## Comment nous protégeons vos informations

- **Chiffrement de bout en bout** pour toutes les données SYNC à l'aide de ChaCha20-Poly1305, avec la clé de chiffrement générée et stockée uniquement sur vos appareils.
- **Chiffrement au repos** dans le stockage cloud — même notre fournisseur d'infrastructure cloud ne voit jamais que du texte chiffré.
- **Chiffrement en transit** à l'aide de HTTPS / TLS pour toutes les communications réseau.
- **Vérification d'intégrité de l'application** pour bloquer l'accès des clients non autorisés au backend SYNC.
- **Sauvegardes chiffrées par mot de passe** à l'aide de la dérivation de clé PBKDF2-SHA256 — chaque sauvegarde est chiffrée avec un mot de passe que vous fournissez ; sans lui, la sauvegarde ne peut pas être déchiffrée.
- **Aucune capacité de déchiffrement côté serveur** — par conception, nous ne pouvons pas lire vos données, même si nous le voulions ou y étions contraints.

Aucun système n'est parfaitement sécurisé, mais nous suivons les meilleures pratiques du secteur et avons conçu BudgeTrak pour réduire au minimum ce à quoi nous avons accès.

## Sous-traitants tiers

BudgeTrak s'appuie sur les sous-traitants tiers suivants. Chacun dispose de sa propre politique de confidentialité régissant la manière dont il traite les données limitées que nous partageons avec lui. Nous énumérons ici les fournisseurs spécifiques afin que cette divulgation soit exhaustive et vérifiable ; le reste de cette politique y fait référence par leur fonction (par exemple, « notre fournisseur d'infrastructure cloud ») pour conserver un texte lisible.

| Service | Fournisseur | Finalité | Ce qu'il voit |
|---|---|---|---|
| Relais des données SYNC chiffrées | Google Firebase Firestore | Base de données cloud pour les blocs chiffrés | Blocs chiffrés uniquement |
| Stockage des photos de reçus chiffrées (SYNC) | Google Firebase Cloud Storage | Stockage d'objets cloud pour les images chiffrées | Blocs chiffrés uniquement |
| Suivi de présence des appareils | Google Firebase Realtime Database | Indicateurs en ligne/hors ligne pour SYNC | Identifiants d'appareil anonymes |
| Authentification backend | Google Firebase Authentication | Connexion anonyme déclenchée uniquement à la première utilisation de SYNC, du Chat d'aide, des fonctions d'IA ou d'un achat payant | Jeton utilisateur anonyme |
| Vérification anti-abus | Google Firebase App Check + Play Integrity | Bloque les clients non autorisés | Attestation de la plateforme |
| Rapport de plantages | Google Firebase Crashlytics | Diagnostic de plantages | Données de plantage, aucune donnée financière |
| Analytique d'utilisation | Google Firebase Analytics | Événements d'utilisation anonymes (précision OCR + battement quotidien) | Comptes et valeurs booléennes uniquement — aucun contenu de transaction, aucune localisation |
| Traitement par IA (fonctions facultatives uniquement) | Google Gemini | Lecture de reçus ; catégorisation des transactions CSV ; assistant Chat d'aide | Contenu de l'image du reçu ; commerçant et montant des transactions bancaires importées ; le texte que vous saisissez dans le Chat d'aide ainsi qu'un extrait pertinent de la documentation d'aide de l'application |
| Achats intégrés et abonnements | Google Play Billing | Abonnements et achats uniques | Informations de paiement (gérées entièrement par Google Play) |
| Publicité (niveau gratuit uniquement) | Google AdMob | Publicité native | Identifiant publicitaire, informations de base sur l'appareil |

Vous pouvez consulter les pratiques de confidentialité de ces fournisseurs à l'adresse [https://policies.google.com/privacy](https://policies.google.com/privacy).

## Fonctions assistées par IA (facultatives)

BudgeTrak propose trois fonctions facultatives assistées par IA. Les deux premières sont disponibles pour les niveaux Payant et Abonné ; la troisième, le Chat d'aide, est disponible pour tous les niveaux (y compris le niveau Gratuit). Les trois sont désactivées par défaut et nécessitent une action explicite de l'utilisateur pour être activées.

### Numérisation de reçus par IA (Abonnés)
Lorsqu'un abonné appuie sur l'icône d'étincelle dans la fenêtre de transaction, BudgeTrak envoie la photo du reçu à notre fournisseur de service d'IA pour en extraire le commerçant, la date, le montant et la catégorie. La réponse est renvoyée directement à votre appareil et stockée uniquement dans votre enregistrement de transaction.

### Catégorisation CSV par IA (niveaux Payant et Abonné, désactivée par défaut)
Lorsqu'elle est activée dans les Paramètres, BudgeTrak envoie le nom du commerçant et le montant des transactions bancaires nouvellement importées à notre fournisseur de service d'IA afin de choisir la catégorie la mieux adaptée à chacune. La date de la transaction **n'est pas** envoyée. Seules les transactions que le catégoriseur local de BudgeTrak ne peut pas classer avec certitude sont envoyées.

### Assistant Chat d'aide (tous les niveaux, désactivé par défaut)
Si vous activez la case du Chat d'aide dans **Paramètres → Confidentialité → Autoriser le chatbot à transmettre et stocker vos messages…** et que vous appuyez sur **Accepter** dans la fenêtre de consentement intégrée à l'application, la fonction Chat d'aide de BudgeTrak vous permet de poser des questions sur le fonctionnement de l'application et de recevoir des réponses générées par IA fondées sur les pages d'aide de l'application. Lorsque la fonction est activée :

- Le texte que vous saisissez est envoyé à notre fournisseur de service d'IA pour générer une réponse. Chaque requête comprend également un court extrait de la documentation d'aide intégrée de l'application afin que l'IA puisse fonder sa réponse sur le comportement réel de BudgeTrak. Aucune donnée financière personnelle, aucun détail de transaction, aucun solde de compte ni paramètre n'est envoyé.
- La transcription complète du chat est également stockée **de façon anonyme** sur notre infrastructure cloud sous un identifiant de chat aléatoire de 128 bits généré sur votre appareil. La transcription est anonyme au sens littéral : nous **n'**enregistrons **pas** votre identifiant utilisateur d'authentification backend, votre identifiant d'appareil, votre adresse IP, votre nom, votre e-mail ni aucun autre identifiant à côté d'elle — seulement l'identifiant de chat, le texte des messages, les horodatages et la version de l'application. Nous utilisons ces transcriptions stockées de façon anonyme pour examiner périodiquement la précision du chatbot et détecter les usages abusifs ; nous ne pouvons pas les rattacher à un utilisateur spécifique. Les transcriptions sont automatiquement supprimées après **7 jours** par une politique de durée de vie (TTL) côté serveur.
- Chaque appareil gère son propre consentement de façon indépendante. La case est désactivée par défaut à l'installation et **n'est pas** synchronisée entre les appareils SYNC. La décocher à tout moment révoque le consentement — les transcriptions déjà présentes sur nos serveurs restent soumises au TTL de 7 jours décrit ci-dessus et seront ensuite supprimées automatiquement, et aucun autre message ne sera téléversé depuis votre appareil.
- Vous pouvez appuyer sur **Effacer** dans la fenêtre du Chat d'aide à tout moment pour téléverser une dernière fois la transcription existante et vider la mémoire tampon locale, en démarrant un nouveau chat avec un nouvel identifiant de chat anonyme. Les messages locaux de plus de 48 heures sont également supprimés automatiquement sur chaque appareil, que vous les effaciez ou non.
- Vous **n'avez pas** besoin d'un abonnement payant, et le Chat d'aide **ne nécessite pas** SYNC. Si vous n'avez pas activé SYNC, BudgeTrak se connectera de façon anonyme la première fois qu'il devra téléverser une transcription, uniquement pour satisfaire l'exigence d'authentification côté serveur ; aucune information personnelle identifiante n'est collectée par cette connexion anonyme.

### Chatbot du site web (techadvantagesupport.github.io)
Notre site web héberge un assistant IA qui répond aux questions des visiteurs sur BudgeTrak, fondé sur la même documentation d'aide intégrée que le Chat d'aide dans l'application. Si vous l'utilisez :

- Le texte que vous saisissez est envoyé à nos serveurs et transmis à notre fournisseur de service d'IA pour générer une réponse. Ne saisissez aucune information personnelle, financière ou de compte — l'assistant n'en a pas besoin et nous vous demandons de ne pas la partager.
- Nous stockons chaque message et réponse pendant **7 jours** au maximum afin d'examiner la précision de l'assistant et de détecter les abus, ainsi qu'un hachage cryptographique à sens unique de votre adresse IP. Le hachage est utilisé **uniquement** pour appliquer une limite quotidienne de messages par visiteur ; nous ne pouvons pas récupérer votre adresse IP à partir de celui-ci, et nous ne stockons aucun nom, e-mail, compte ni identifiant d'appareil avec les chats du site web.
- Aucun compte ni connexion n'est requis, et l'utilisation du chatbot du site web est entièrement facultative.

### Ce qui n'est jamais envoyé au fournisseur de service d'IA
- Vos soldes de compte ou vos totaux
- Votre historique de transactions (autre que les lignes importées spécifiques ou le reçu en cours de traitement)
- Vos clés de chiffrement, vos identifiants d'appareil ou vos jetons d'authentification
- Vos photos de reçus (elles ne sont envoyées que par la Numérisation de reçus ci-dessus, jamais par la Catégorisation CSV ni par le Chat d'aide)
- Toute donnée provenant d'une quelconque fonction de BudgeTrak, sauf si vous avez explicitement opté pour cette fonction spécifique

### Comment vos données sont protégées
- Toutes les requêtes sont chiffrées en transit (HTTPS/TLS).
- Pour la Numérisation de reçus et la Catégorisation CSV, le fournisseur de service d'IA supprime les données de requête et de réponse une fois la requête terminée ; rien n'est stocké sur les serveurs du fournisseur pour ces fonctions. Conformément à la configuration par défaut du fournisseur, **vos données ne sont pas utilisées pour entraîner les modèles d'IA du fournisseur**.
- Pour le Chat d'aide, vos messages saisis et les réponses de l'IA sont stockés par BudgeTrak (et non par le fournisseur de service d'IA) pendant 7 jours au maximum pour l'examen de précision/abus décrit ci-dessus, puis sont automatiquement supprimés. Le fournisseur d'IA ne conserve pas la requête après la génération de la réponse.
- Toutes les fonctions d'IA peuvent être désactivées à tout moment dans les Paramètres, ce qui revient au comportement entièrement sur l'appareil de BudgeTrak (ou au lien d'échappement par e-mail intégré à l'application pour le Chat d'aide).

Les utilisateurs du niveau gratuit ont accès au **Chat d'aide** (avec consentement) mais pas à la **Numérisation de reçus par IA** ni à la **Catégorisation CSV par IA**.

## Vos droits et choix

Vous avez un contrôle total sur vos données dans BudgeTrak.

- **Tout supprimer** : Désinstaller BudgeTrak supprime toutes les données stockées localement sur votre appareil. Si vous utilisez également SYNC, quittez ou dissolvez d'abord votre groupe SYNC depuis l'écran SYNC pour supprimer la copie dans le cloud.
- **Quitter un groupe SYNC** : Appuyez sur « Quitter le groupe » sur l'écran SYNC. Vos données locales sont conservées ; les données cloud liées à votre appareil sont supprimées.
- **Dissoudre un groupe SYNC** (administrateur uniquement) : Appuyez sur « Dissoudre le groupe » sur l'écran SYNC. Toutes les données cloud du groupe sont définitivement supprimées ; chaque appareil conserve sa copie locale.
- **Exporter vos données** : Utilisez la fonction Enregistrer sur l'écran Transactions pour exporter vos transactions au format CSV, Excel ou PDF. Les sauvegardes effectuées depuis les Paramètres incluent toutes vos données budgétaires dans un seul fichier.
- **Désactiver le rapport de plantages et la télémétrie d'utilisation** : Ouvrez **Paramètres → Confidentialité → Envoyer les rapports de plantage et les données d'utilisation anonymes** dans BudgeTrak et décochez la case. Le changement prend effet immédiatement — il est indiqué au service de rapport de plantages et au service d'analytique de cesser de collecter toute donnée de votre appareil, y compris le battement quotidien et les événements de précision OCR.
- **Révoquer le consentement au Chat d'aide** : Ouvrez **Paramètres → Confidentialité → Autoriser le chatbot à transmettre et stocker vos messages…** dans BudgeTrak et décochez la case. Aucun autre message de votre appareil ne sera téléversé. Toute transcription stockée de façon anonyme déjà présente sur nos serveurs continue d'être supprimée automatiquement après la période de conservation de 7 jours décrite ci-dessus ; comme elles sont stockées sans votre identité, nous ne pouvons pas supprimer sur demande les transcriptions passées d'un utilisateur spécifique.
- **Limiter le suivi publicitaire** : Réinitialisez ou limitez votre identifiant publicitaire Android dans les paramètres de votre appareil sous Confidentialité → Annonces.

Si vous souhaitez que nous vous confirmions quelles données nous détenons à votre sujet (remarque : dans la quasi-totalité des cas, la réponse est « rien qui vous identifie personnellement ») ou si vous avez toute autre demande relative à la confidentialité, contactez-nous à **support@techadvantageapps.com**.

## Suppression des données

**BudgeTrak n'a pas de compte utilisateur au sens habituel — pas d'inscription, pas de nom d'utilisateur ni de mot de passe, et nous ne collectons jamais votre nom, votre adresse e-mail ou votre numéro de téléphone.** Le seul identifiant backend est un jeton anonyme, généré aléatoirement, créé lors de la première utilisation de SYNC, du Chat d'aide, des fonctions d'IA ou d'un achat, et il n'est jamais lié à votre identité réelle. Combiné au chiffrement de bout en bout et aux identifiants de groupe SYNC générés aléatoirement, cela signifie que la suppression s'effectue **dans l'application et automatiquement** (détaillée ci-dessous) plutôt que par une demande par e-mail — nous n'avons ni nom ni adresse e-mail pour retrouver vos enregistrements.

Vous pouvez demander la suppression de vos données BudgeTrak par l'une des options suivantes :

### 1. Suppression depuis l'application (administrateur d'un groupe SYNC)
Ouvrez BudgeTrak → Paramètres → SYNC → **Dissoudre le groupe**. Cela supprime définitivement toutes les données côté serveur du groupe : transactions, catégories, dépenses récurrentes, sources de revenus, objectifs d'épargne, entrées d'amortissement, grand livre de période, photos de reçus chiffrées et métadonnées du groupe. La cascade est exécutée par une fonction côté serveur qui supprime les données de notre infrastructure cloud. Chaque appareil membre conserve sa copie locale, à moins qu'il ne désinstalle également l'application.

### 2. Retrait depuis l'application (membre d'un groupe SYNC)
Ouvrez BudgeTrak → Paramètres → SYNC → **Quitter le groupe**. Votre appareil est marqué comme retiré dans la liste des appareils du groupe, votre enregistrement de présence en temps réel est supprimé et les clés de chiffrement de votre appareil pour le groupe sont effacées. Les données partagées elles-mêmes restent dans le groupe pour les membres restants ; si vous souhaitez que le groupe entier soit supprimé, l'administrateur doit le dissoudre.

### 3. Suppression locale uniquement
Désinstaller BudgeTrak supprime immédiatement toutes les données présentes sur l'appareil (transactions, paramètres, photos de reçus, sauvegardes chiffrées stockées dans le dossier privé de l'application). Si vous n'avez utilisé BudgeTrak qu'en mode solo (sans SYNC), aucune donnée côté cloud n'a jamais existé et la désinstallation achève entièrement la suppression.

### 4. Suppression automatique
Les groupes SYNC qui n'ont été ouverts par aucun appareil membre pendant 90 jours consécutifs sont automatiquement et définitivement supprimés par un processus de nettoyage côté serveur. Cela inclut toutes les transactions, photos chiffrées et métadonnées. Il n'existe aucune récupération après ce nettoyage automatique ; veillez à disposer d'une sauvegarde locale avant de laisser un groupe devenir inactif.

### Pourquoi nous ne proposons pas de suppression manuelle par e-mail
BudgeTrak n'associe délibérément pas vos données cloud à votre nom, votre adresse e-mail ou tout identifiant que nous pourrions utiliser pour retrouver « vos » enregistrements sur demande. L'authentification anonyme, le chiffrement de bout en bout et les identifiants de groupe générés aléatoirement sont ce qui rend possibles les garanties de confidentialité de cette politique — mais cette même conception signifie que si vous nous écrivez pour demander la suppression d'un groupe spécifique, nous n'avons aucun moyen de vérifier que le groupe vous appartient ni même de le localiser parmi les blocs chiffrés de nos serveurs.

Si vous avez perdu l'accès à votre appareil ou à un groupe dont vous ne pouvez plus joindre l'administrateur, le nettoyage par inactivité de 90 jours décrit ci-dessus est le mécanisme de suppression. Assurez-vous de disposer d'une sauvegarde locale de toutes les données que vous souhaitez conserver avant l'expiration de cette fenêtre.

Ce que la suppression **n'affecte pas** : les enregistrements de plantage anonymes (conservés par le fournisseur de rapport de plantages pendant 90 jours conformément à sa politique standard, indépendamment des actions effectuées dans l'application) et les identifiants publicitaires (gérés par Android au niveau de l'appareil — réinitialisez-les via les paramètres de votre appareil).

## Conservation des données

- **Les données sur l'appareil** sont conservées jusqu'à ce que vous les supprimiez ou désinstalliez l'application.
- **Les données cloud SYNC** sont automatiquement supprimées 90 jours après la dernière activité sur un groupe, et immédiatement supprimées lorsqu'un groupe est dissous.
- **Les transcriptions du Chat d'aide** sont stockées de façon anonyme et automatiquement supprimées **7 jours** après la dernière mise à jour par une politique de durée de vie (TTL) côté serveur. Les copies locales sur votre appareil sont supprimées après 48 heures dans tous les cas.
- **Les rapports de plantage** sont conservés par le fournisseur de rapport de plantages conformément à ses politiques de conservation standard (actuellement 90 jours pour les données de plantage).
- **Les photos de reçus dans le stockage cloud** suivent la période de conservation que l'administrateur de votre groupe définit dans les Paramètres, ou sont conservées indéfiniment si aucune période de conservation n'est configurée. Elles sont immédiatement supprimées lorsque vous retirez la transaction ou la photo correspondante.

## Confidentialité des mineurs

BudgeTrak est un outil de finances personnelles destiné aux utilisateurs âgés de 13 ans et plus. Nous ne collectons pas sciemment d'informations personnelles auprès d'enfants de moins de 13 ans. Si vous pensez qu'un enfant de moins de 13 ans nous a fourni des informations personnelles, veuillez nous contacter à **support@techadvantageapps.com** et nous prendrons des mesures pour les supprimer.

## Utilisateurs internationaux

BudgeTrak est publiée depuis les États-Unis. Si vous utilisez l'application depuis un pays autre que les États-Unis, veuillez noter que toute donnée que vous choisissez de synchroniser dans le cloud (qui est chiffrée avant de quitter votre appareil) peut être relayée via des serveurs exploités par nos sous-traitants tiers aux États-Unis ou dans d'autres pays où ils maintiennent une infrastructure. En utilisant la fonction SYNC de BudgeTrak, vous consentez à ce relais.

## Modifications de cette politique

Nous pouvons mettre à jour cette politique de confidentialité de temps à autre, en particulier lorsque nous ajoutons ou supprimons des fonctions qui affectent les données collectées. Lorsque nous apportons des modifications importantes, nous mettons à jour la date de « Dernière mise à jour » en haut de cette page et, le cas échéant, vous en informons dans l'application. Votre utilisation continue de BudgeTrak après une mise à jour de la politique constitue une acceptation de la politique révisée.

## Nous contacter

Si vous avez des questions sur cette politique de confidentialité ou sur les pratiques de BudgeTrak en matière de données, veuillez contacter :

**Tech Advantage LLC**
E-mail : **support@techadvantageapps.com**

Nous répondrons aux demandes légitimes relatives à la confidentialité dans un délai raisonnable, généralement sous 30 jours.
