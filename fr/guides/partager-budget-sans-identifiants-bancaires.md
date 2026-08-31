---
layout: guide
lang: fr
group: banklogins
permalink: /fr/guides/partager-budget-sans-identifiants-bancaires/
title: "Comment partager un budget en couple sans partager ses identifiants bancaires | BudgeTrak"
short_title: "Partager sans identifiants"
h1: "Comment partager un budget avec ton ou ta partenaire sans partager vos identifiants bancaires"
kicker: "Confidentialité et argent partagé"
description: "Vous pouvez tenir un budget du foyer sur deux téléphones sans que personne ne saisisse d'identifiants bancaires où que ce soit. Voici comment ça marche, ce qui est synchronisé et quels sont les vrais compromis."
standfirst: "Des finances communes n'exigent pas des mots de passe communs. Voici la mécanique d'un budget partagé qui ne touche jamais ta banque."
hero: /assets/guides/hero-privacy.jpg
hero_alt: "Un couple, chacun avec son téléphone, partage un budget du foyer"
published: "2026-08-31"
reading_time: 7
faq:
  - q: "Peut-on partager un budget sans relier ses comptes bancaires ?"
    a: "Oui. Un budget a besoin de trois données — revenus, engagements récurrents et dépenses — et aucune n'exige un accès bancaire. BudgeTrak synchronise ces trois données directement entre tes appareils avec un chiffrement de bout en bout, donc aucune connexion bancaire n'existe à aucun moment."
  - q: "Quelles données sont réellement synchronisées entre les partenaires ?"
    a: "Votre budget : revenus, dépenses récurrentes, objectifs d'épargne, catégories et opérations, chacune attribuée à l'appareil qui l'a saisie. Le tout chiffré de bout en bout, c'est-à-dire illisible en transit et illisible au repos sur nos serveurs."
  - q: "Mon ou ma partenaire peut-il voir mon compte bancaire personnel ?"
    a: "Non, car BudgeTrak n'a accès au compte bancaire de personne. Les membres voient le budget partagé du foyer et les opérations qui y sont saisies, rien de plus."
  - q: "Un budget partagé sans banque demande-t-il plus de travail ?"
    a: "Un peu. Compte environ une minute de saisie par jour, ou un import CSV hebdomadaire. Si ta banque envoie des notifications d'achat, la formule Abonné peut les convertir automatiquement en entrées en attente, ce qui supprime l'essentiel du travail manuel."
  - q: "Combien de personnes peuvent partager un budget ?"
    a: "Jusqu'à cinq appareils dans un groupe SYNC. Une personne s'abonne à 4,99 $ par mois, les autres rejoignent gratuitement."
related:
  - url: /fr/guides/application-budget-pour-couples/
    title: "La meilleure appli de budget pour couples"
    blurb: "Le dossier complet, y compris là où nous ne convenons pas."
  - url: /fr/guides/budget-sans-connexion-bancaire/
    title: "Budgéter sans connexion bancaire"
    blurb: "Le même principe, pour une seule personne."
  - url: /fr/guides/application-budget-familial/
    title: "Un budget sur tous les téléphones"
    blurb: "Ajouter ados et autres adultes."
  - url: /fr/guides/budget-sur-explique/
    title: "Ce que veut dire « budget sûr »"
    blurb: "Le chiffre auquel tout cela sert."
---

L'hypothèse inscrite dans presque tous les produits de finances partagées, c'est que réunir l'argent de deux personnes exige de réunir l'accès bancaire de deux personnes. C'est faux. Cela exige de réunir leurs *chiffres*, ce qui est bien plus petit et bien moins sensible.

Ce guide, c'est la mécanique : ce dont un budget partagé a réellement besoin, ce que BudgeTrak envoie et où, et ce que tu abandonnes en ne connectant pas de banque.

## Un budget a besoin de trois données. Aucune n'est ta banque.

Écris ce qu'un budget calcule vraiment :

1. **Ce qui entre** — tes revenus, et quand ils tombent.
2. **Ce qui est déjà engagé** — loyer, assurances, abonnements, objectifs d'épargne, la facture annuelle que tu oublies chaque année.
3. **Ce qui est sorti jusqu'ici** — les dépenses depuis le début de la période.

C'est tout. Avec ces trois éléments, l'arithmétique est déterministe. L'agrégation bancaire est un *confort de saisie* pour la donnée 3. Elle ne fait pas partie du calcul et ne joue aucun rôle dans les données 1 et 2 — là où, précisément, la plupart des budgets de foyer déraillent.

Autrement dit : connecter ta banque rend la saisie plus facile. Ça ne rend pas ton budget plus juste. On confond souvent les deux.

## Ce que « partagé » veut dire sans banque au milieu

Dans une appli à agrégation, ça se passe ainsi : vous reliez tous les deux vos comptes, l'agrégateur récupère vos deux historiques sur un serveur, et l'appli affiche une vue commune. L'objet partagé est *une copie serveur de deux historiques bancaires*.

Dans BudgeTrak, l'objet partagé est le document du budget lui-même — revenus, factures, objectifs, opérations — répliqué entre vos propres appareils. Une personne crée le groupe SYNC, l'autre rejoint avec un code. Ensuite les deux téléphones portent le même budget et se mettent à jour mutuellement en temps réel.

La différence compte surtout dans le pire scénario. Si nos serveurs étaient compromis demain, ce qu'un attaquant détiendrait serait du texte chiffré : les données SYNC sont chiffrées sur ton appareil avant de partir et ne peuvent être déchiffrées que par les appareils de ton groupe. Nous ne pouvons pas les lire — ce qui signifie aussi que nous ne pouvons pas les récupérer si tous les appareils du groupe sont perdus.

<figure class="shot">
<img src="/assets/tour/fr/sync.webp" alt="Écran SYNC de BudgeTrak avec les membres du foyer" width="540" height="960" loading="lazy">
<figcaption>Jusqu'à cinq appareils sur un budget chiffré, avec attribution par membre.</figcaption>
</figure>

<div class="note">
<p><strong>Une limite honnête.</strong> « Chiffré de bout en bout » s'applique à SYNC. Cela ne veut pas dire que l'appli ne parle jamais au réseau : les fonctions d'IA optionnelles (scan de reçus, catégorisation CSV, chat d'aide) envoient ce que tu leur confies pour traitement, et c'est le marché quand tu utilises ces fonctions précises. Tout ce qui est décrit dans ce guide fonctionne sans y toucher.</p>
</div>

## Faire entrer les dépenses : les trois voies

Sans flux bancaire, les opérations arrivent de trois façons. La plupart des foyers finissent par en utiliser deux.

### 1. Saisir sur le moment
Le widget d'accueil accepte une dépense en deux appuis sans ouvrir l'appli. Cela semble être l'option fastidieuse et c'est celle dont on doute le plus, mais le coût réel tourne autour de 40 secondes par jour — avec un effet secondaire sous-estimé : tu remarques ce que tu dépenses *pendant* que tu le dépenses, et c'est là que se joue l'essentiel du changement de comportement pour lequel on achète une appli de budget.

### 2. Importer un relevé
Télécharge un CSV chez ta banque quand ça t'arrange et importe-le. La détection de doublons rapproche ce que tu as déjà saisi à la main, la reconnaissance des commerçants apprend tes habitudes. Compris dans l'achat unique à 9,99 $. C'est le rythme « rattraper le dimanche », et pour un couple qui ne veut pas saisir tous les jours, ça marche bien.

### 3. Laisser travailler les notifications de ta banque
Si ton appli bancaire t'envoie déjà une alerte au paiement par carte, cette alerte contient déjà le commerçant et le montant. BudgeTrak peut lire ces notifications sur ton appareil et les transformer en entrées **en attente** — quelques secondes après l'achat, des jours avant que l'opération n'apparaisse sur un relevé.

Cela mérite d'être précisé, car cela ressemble à ce que nous venons d'exclure. Ce n'en est pas. Aucun identifiant bancaire, aucun agrégateur, aucune autorisation SMS. L'appli lit des notifications que ta banque envoie déjà à ton propre téléphone, en extrait le montant et le commerçant, et met en file une entrée en attente que tu valides avant qu'elle ne touche ton budget. Chaque appareil ne voit que son propre flux de notifications. Formule Abonné.

<figure class="shot">
<img src="/assets/tour/fr/transactions.webp" alt="Liste des opérations dans BudgeTrak" width="540" height="960" loading="lazy">
<figcaption>Quelle que soit la voie d'arrivée, tout atterrit dans le même registre partagé.</figcaption>
</figure>

## Attribution sans surveillance

Chaque opération enregistre l'appareil qui l'a saisie. C'est volontairement léger : cela existe pour que, lorsque le chiffre quotidien baisse de 80 €, l'un ou l'autre voie pourquoi sans avoir à demander. Ce n'est pas une fonction de contrôle, et il n'y a pas de classement des dépenses par personne, parce que ce serait un autre produit et, en général, une relation moins bonne.

## Ce que tu abandonnes vraiment

Trois choses, dites clairement :

- **La capture automatique de tout, partout.** La capture par notification couvre les cartes dont la banque envoie des alertes. Les espèces, et les banques qui ne notifient pas, demandent toujours saisie ou import.
- **L'historique rétroactif dès le premier jour.** Un agrégateur récupère douze mois dès la connexion. Ici, tu importerais un CSV pour le même résultat.
- **Le rapprochement automatique avec ton solde bancaire.** BudgeTrak suit le budget que tu lui as décrit, pas ton solde réel. S'ils divergent, tu rapproches au prochain import.

Si ces trois points sont rédhibitoires, une appli à agrégation est sincèrement le meilleur outil et tu devrais l'utiliser.

## Le configurer ensemble

Quinze minutes, une fois, sur un téléphone :

1. Saisis les revenus — y compris les irréguliers ; le moteur gère les revenus variables et les factures groupées.
2. Saisis les dépenses récurrentes avec leurs vraies dates d'échéance.
3. Ajoute les objectifs d'épargne et tout gros montant que tu étales sur plusieurs mois.
4. Active SYNC et fais rejoindre ton ou ta partenaire avec le code.

Ensuite vous regardez tous les deux le même chiffre quotidien. La première semaine est généralement inconfortable, parce que le chiffre est plus petit que le solde bancaire que vous utilisiez tous les deux. Cet écart, c'est justement le point — ce sont les engagements que vous dépensiez deux fois.
