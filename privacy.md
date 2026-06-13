---
layout: default
title: BudgeTrak Privacy Policy
---

<p align="right"><a href="/es/privacy"><b>Español</b></a> · <a href="/de/privacy"><b>Deutsch</b></a> · <a href="/fr/privacy"><b>Français</b></a></p>

# BudgeTrak Privacy Policy

**Effective date:** April 11, 2026
**Last updated:** May 20, 2026

## Plain-English Summary

BudgeTrak is a personal budgeting app. Your financial data lives on your device. If you choose to enable the SYNC feature to share your budget across multiple devices in your household, that data is end-to-end encrypted before it leaves your device — neither we nor any cloud provider can read your transactions, balances, or merchant names. If you opt in to the in-app Help Chat assistant, the text you type into it is sent to our AI service provider to generate answers and is stored **anonymously** on our servers for up to 7 days for quality review (not linked to your identity). Your financial data is never shared with advertisers or used to profile you. The free tier is supported by ads from Google AdMob, which uses your device's advertising ID to show personalized ads (resettable in your device settings; ads removed entirely if you upgrade or subscribe). The full policy below explains exactly what is collected, where it goes, and how to delete it.

## Who We Are

BudgeTrak is published by **Tech Advantage LLC** ("we", "us", "our"). You can contact us at **support@techadvantageapps.com** for any privacy-related questions or requests.

## Information We Collect

We try to collect as little as possible, and we keep most of it on your device only.

### On-Device Data (Always Local)

When you use BudgeTrak, the following information is stored on your device in the app's private storage:

- **Transactions** you record: amount, date, merchant or source name, description, category, and any notes you add.
- **Budget configuration**: your income sources, recurring expenses, savings goals, amortization entries, and your chosen budget period (daily, weekly, or monthly).
- **App settings**: currency symbol, date format, theme, language preference, and similar display choices.
- **Receipt photos** you choose to attach to a transaction (optional).
- **Auto-backup files** stored in a location on your device that you choose.

This data never leaves your device unless you explicitly enable a feature that sends it elsewhere (described below). If you uninstall BudgeTrak, all on-device data is deleted by Android automatically.

### Cloud Sync Data (Only If You Opt In)

BudgeTrak includes an optional feature called **SYNC** that lets you share a single household budget across up to five devices. SYNC is **off by default** and only activates if you explicitly create or join a SYNC group.

If you enable SYNC, the following happens:

- An encryption key is generated on your device when you create a group, or shared securely via a 6-character pairing code when you join one.
- Your transactions, income sources, recurring expenses, savings goals, amortization entries, app settings, and receipt photos are encrypted **on your device** using ChaCha20-Poly1305 encryption with that key.
- Only the encrypted data is uploaded to our cloud infrastructure provider for relay to other devices in your group.
- The encryption key never leaves your devices. Our cloud infrastructure provider, our servers, and any third party with access to the cloud storage **cannot** decrypt your financial data — they can only see encrypted blobs.
- Each linked device decrypts the data locally using the shared key.

When you leave a SYNC group or dissolve it, your local data is preserved on your device but the cloud copy is deleted (with a 90-day cleanup window for orphan data).

### Diagnostic and Crash Data

To keep BudgeTrak stable and identify bugs, we use anonymous **crash reporting** and **usage telemetry** services from our cloud infrastructure provider. Both are **on by default** and share a single opt-out at **Settings → Privacy → Send crash reports and anonymous usage data**. Unchecking that box stops both immediately.

When this collection is enabled, the data we collect includes:

- Crash stack traces and error messages.
- Anonymous device information (model, OS version, app version).
- An anonymous backend authentication user ID — present only if you have used a feature that requires backend authentication (SYNC, Help Chat, AI Receipt Scanning, AI CSV Categorization, or a paid purchase). A random identifier generated on first use, not your name or email. Users who never use any of those features never receive a backend user ID at all.
- Diagnostic counters: the number of transactions, recurring expenses, and period-ledger entries you have; sync status (`healthy`, `dead`, or `off`); the number of devices in your SYNC group; and the date of your last period refresh.
- A **one-way hash digest** of your available cash balance (computed locally as a hex digest before being sent). The actual cash value never leaves your device, and the hash cannot be reversed to recover the original number.
- Timestamped lifecycle events like "listener started," "token refreshed," or "period boundary crossed" used to debug sync issues.
- Two anonymous usage events: **`ocr_feedback`** records whether you changed the merchant, date, or amount on a transaction populated by AI receipt scanning (deltas and booleans only — never the values themselves), and **`health_beacon`** records once a day whether your SYNC listener is connected and the *count* of records on your device.
- Standard analytics startup events (`first_open`, `session_start`, `app_update`) recording that the app was used, but no information about *what* you did inside it.

Crash and telemetry data do **not** include the contents of your transactions, merchant names, amounts, dates, descriptions, categories, receipt photos, encryption keys, or any other personal financial information. We hash the only piece of financial data that touches diagnostics (your cash balance) so that even we cannot read it. We have also disabled IP-based country/region derivation in our analytics configuration, so no approximate location is collected.

If you disable diagnostic reporting, none of the above is collected — the daily heartbeat used to confirm devices are healthy and the OCR-accuracy events used to improve receipt scanning are both skipped. We recommend leaving it on so we can detect and fix bugs that affect real users, but the choice is yours.

### Authentication and Anti-Abuse

BudgeTrak signs you in to our backend using **anonymous authentication** (no email or password required) only when you first use a feature that needs it: **SYNC** (joining or creating a household sync group), **Help Chat** (sending a message to the AI assistant), **AI Receipt Scanning**, **AI CSV Categorization**, or completing a **paid purchase or subscription**. Until you use one of those features, your device has no backend user ID — the app runs entirely on-device with no authenticated session. The first time you do use one, a random anonymous token is generated, persists for the life of that install, and is used only to satisfy our server's authentication requirement on the corresponding feature. Your device is also verified using the Android platform's app-integrity attestation to prevent unauthorized clients from accessing the cloud relay. Neither of these systems collects personal information about you.

### Subscription and Purchase Data

If you upgrade to a paid tier or subscribe to BudgeTrak Premium, the purchase is processed entirely by **Google Play Billing** (the standard Android in-app purchase system). We do not see your payment method, credit card number, or billing address — Google Play handles all of that. We only receive a confirmation that your purchase is valid, used to unlock the corresponding features in the app.

### Advertising (Free Tier Only)

The free tier of BudgeTrak displays native ads served through an advertising network. The network may collect a limited Android advertising identifier and basic device information to serve ads. You can reset or limit your **Android advertising identifier** in your device settings at any time. If you upgrade to a paid tier or subscribe to Premium, ads are removed entirely.

### What We Do **Not** Collect

We want to be specific about this. BudgeTrak does **not** collect:

- Your name, email address, phone number, or any other directly identifying personal information.
- Your physical location, GPS coordinates, or IP address (beyond what the platform services receive automatically for routing).
- Your contacts, calendar, photos library (other than receipt photos you explicitly attach), call history, SMS messages, or browsing history.
- Your bank account credentials, routing numbers, or login details for any financial institution.
- Any health, fitness, or biometric data.

## How We Use Information

We use the limited information we collect for exactly these purposes, and nothing else:

- **To provide the app's core functionality** (calculate your budget, sync data across your devices if you opted in, display your transactions).
- **To diagnose crashes and bugs** so we can fix them in the next release.
- **To verify the integrity of your subscription** if you have upgraded.
- **To serve ads** on the free tier through our advertising network.

We do **not**:

- Sell your data to anyone, ever, for any purpose.
- Share your data with data brokers, marketing networks, or analytics companies (other than the third-party processors listed below).
- Use your financial data to train machine learning models or AI systems.
- Use your financial data for advertising or to build a profile of you.

## How We Protect Your Information

- **End-to-end encryption** for all SYNC data using ChaCha20-Poly1305, with the encryption key generated and stored only on your devices.
- **Encrypted at rest** in cloud storage — even our cloud infrastructure provider only ever sees ciphertext.
- **Encrypted in transit** using HTTPS / TLS for all network communication.
- **App-integrity verification** to block unauthorized clients from accessing the SYNC backend.
- **Password-encrypted backups** using PBKDF2-SHA256 key derivation — every backup is encrypted with a password you provide; without it, the backup cannot be decrypted.
- **No server-side decryption capability** — by design, we cannot read your data even if we wanted to or were compelled to.

No system is perfectly secure, but we follow industry best practices and have designed BudgeTrak to minimize what we ever have access to.

## Third-Party Processors

BudgeTrak relies on the following third-party processors. Each has its own privacy policy that governs how they handle the limited data we share with them. We list the specific providers here so this disclosure is exhaustive and verifiable; the rest of this policy refers to them by their function (e.g., "our cloud infrastructure provider") to keep the prose readable.

| Service | Provider | Purpose | What it sees |
|---|---|---|---|
| Encrypted SYNC data relay | Google Firebase Firestore | Cloud database for encrypted blobs | Encrypted blobs only |
| Encrypted receipt photo storage (SYNC) | Google Firebase Cloud Storage | Cloud object storage for encrypted images | Encrypted blobs only |
| Device presence tracking | Google Firebase Realtime Database | Online/offline indicators for SYNC | Anonymous device IDs |
| Backend authentication | Google Firebase Authentication | Anonymous sign-in triggered only by first use of SYNC, Help Chat, AI features, or a paid purchase | Anonymous user token |
| Anti-abuse verification | Google Firebase App Check + Play Integrity | Blocks unauthorized clients | Platform attestation |
| Crash reporting | Google Firebase Crashlytics | Crash diagnostics | Crash data, no financial data |
| Usage analytics | Google Firebase Analytics | Anonymous usage events (OCR accuracy + daily heartbeat) | Counts and booleans only — no transaction content, no location |
| AI processing (opt-in features only) | Google Gemini | Receipt reading; CSV transaction categorization; Help Chat assistant | Receipt image contents; merchant and amount of imported bank transactions; the text you type into Help Chat plus a relevant excerpt of the app's help documentation |
| In-app purchases and subscriptions | Google Play Billing | Subscription and one-time purchases | Payment info (handled entirely by Google Play) |
| Advertising (free tier only) | Google AdMob | Native advertising | Advertising ID, basic device info |

You can review the privacy practices of these providers at [https://policies.google.com/privacy](https://policies.google.com/privacy).

## AI-Assisted Features (Opt-In)

BudgeTrak offers three optional AI-assisted features. The first two are available to Paid and Subscriber tiers; the third, Help Chat, is available to all tiers (including Free). All three are off by default and require an explicit user action to enable.

### AI Receipt Scanning (Subscribers)
When a subscriber taps the sparkle icon in the transaction dialog, BudgeTrak sends the receipt photo to our AI service provider to extract the merchant, date, amount, and category. The response is returned directly to your device and stored only in your transaction record.

### AI CSV Categorization (Paid and Subscriber tiers, off by default)
When enabled in Settings, BudgeTrak sends the merchant name and amount of newly-imported bank transactions to our AI service provider to choose the best-matching category for each one. The transaction date is **not** sent. Only transactions that BudgeTrak's on-device categorizer cannot confidently classify are sent.

### Help Chat Assistant (All tiers, off by default)
If you enable the Help Chat checkbox in **Settings → Privacy → Allow Chatbot to transmit and store your messages…** and tap **Accept** on the in-app consent dialog, BudgeTrak's Help Chat feature lets you type questions about how the app works and receive AI-generated answers grounded in the app's help pages. When the feature is enabled:

- The text you type is sent to our AI service provider to generate a reply. Each request also includes a short excerpt from the app's built-in help documentation so the AI can ground its answer in BudgeTrak's actual behavior. No personal financial data, transaction details, account balances, or settings are sent.
- The full chat transcript is also stored **anonymously** on our cloud infrastructure under a random 128-bit chat ID generated on your device. The transcript is anonymous in the literal sense: we do **not** record your backend authentication user ID, device ID, IP address, name, email, or any other identifier alongside it — only the chat ID, the message text, timestamps, and the app version. We use these anonymously stored transcripts to periodically review the chatbot's accuracy and detect abusive use; we cannot tie them back to any specific user. Transcripts are automatically deleted after **7 days** by a server-side time-to-live policy.
- Each device manages its own consent independently. The checkbox is off by default on install and is **not** synced between SYNC devices. Unchecking it at any time revokes consent — past transcripts already on our servers remain subject to the 7-day TTL above and will then be deleted automatically, and no further messages will be uploaded from your device.
- You can tap **Clear** in the Help Chat dialog at any time to immediately upload the existing transcript one last time and wipe the local buffer, starting a fresh chat with a new anonymous chat ID. Local messages older than 48 hours are also pruned automatically on each device regardless of whether you clear them.
- You do **not** need a paid subscription, and Help Chat does **not** require SYNC. If you have not enabled SYNC, BudgeTrak will sign in anonymously the first time it needs to upload a transcript, solely so our server-side authentication requirement is satisfied; no personally-identifying information is collected through this anonymous sign-in.

### Website Chatbot (techadvantagesupport.github.io)
Our website hosts an AI assistant that answers visitor questions about BudgeTrak, grounded in the same built-in help documentation as the in-app Help Chat. If you use it:

- The text you type is sent to our servers and forwarded to our AI service provider to generate a reply. Do not enter personal, financial, or account information — the assistant does not need it and we ask you not to share it.
- We store each message and reply for up to **7 days** to review the assistant's accuracy and detect abuse, together with a one-way cryptographic hash of your IP address. The hash is used **only** to enforce a daily per-visitor message limit; we cannot recover your IP address from it, and we store no name, email, account, or device identifier with website chats.
- No account or sign-in is required, and using the website chatbot is entirely optional.

### What's never sent to the AI service provider
- Your account balances or totals
- Your historical transactions (other than the specific imported rows or receipt being processed)
- Your encryption keys, device identifiers, or authentication tokens
- Your receipt photos (they are only sent by Receipt Scanning above, never by CSV Categorization or Help Chat)
- Any data from any BudgeTrak feature unless you have explicitly opted in to that specific feature

### How your data is protected
- All requests are encrypted in transit (HTTPS/TLS).
- For Receipt Scanning and CSV Categorization, the AI service provider deletes request and response data once the request completes; nothing is stored on the provider's servers for these features. Per the provider's default configuration, **your data is not used to train the provider's AI models**.
- For Help Chat, your typed messages and the AI's replies are stored by BudgeTrak (not by the AI service provider) for up to 7 days for the accuracy/abuse review described above, and are then automatically deleted. The AI provider does not retain the request after the response is generated.
- All AI features can be disabled in Settings at any time, which falls back to BudgeTrak's fully on-device behavior (or to the in-app email escape link for Help Chat).

Free-tier users have access to **Help Chat** (with consent) but not to **AI Receipt Scanning** or **AI CSV Categorization**.

## Your Rights and Choices

You have full control over your data in BudgeTrak.

- **Delete everything**: Uninstalling BudgeTrak removes all locally stored data from your device. If you also use SYNC, leave or dissolve your SYNC group from the SYNC screen first to remove the cloud copy.
- **Leave a SYNC group**: Tap "Leave Group" on the SYNC screen. Your local data is preserved; cloud data tied to your device is removed.
- **Dissolve a SYNC group** (admin only): Tap "Dissolve Group" on the SYNC screen. All cloud data for the group is permanently deleted; each device retains its local copy.
- **Export your data**: Use the Save feature on the Transactions screen to export your transactions in CSV, Excel, or PDF format. Backups via Settings include all your budget data in a single file.
- **Disable crash reporting and usage telemetry**: Open **Settings → Privacy → Send crash reports and anonymous usage data** in BudgeTrak and uncheck the box. The change takes effect immediately — crash reporting and analytics are both told to stop collecting any data from your device, including the daily heartbeat and the OCR-accuracy events.
- **Revoke Help Chat consent**: Open **Settings → Privacy → Allow Chatbot to transmit and store your messages…** in BudgeTrak and uncheck the box. No further messages from your device will be uploaded. Any anonymously stored transcripts already on our servers continue to be deleted automatically after the 7-day retention period described above; because they are stored without your identity, we cannot delete a specific user's past transcripts on request.
- **Limit ad tracking**: Reset or limit your Android advertising identifier in your device settings under Privacy → Ads.

If you want us to confirm what data we hold about you (note: in nearly all cases, the answer is "nothing personally identifying") or have any other privacy request, contact us at **support@techadvantageapps.com**.

## Data Deletion

You can request deletion of your BudgeTrak data through any of the following options:

### 1. In-app deletion (admin of a SYNC group)
Open BudgeTrak → Settings → SYNC → **Dissolve Group**. This permanently deletes all server-side data for the group: transactions, categories, recurring expenses, income sources, savings goals, amortization entries, period ledger, encrypted receipt photos, and group metadata. The cascade is performed by a server-side function that removes data from our cloud infrastructure. Each member device retains its local copy unless they also uninstall the app.

### 2. In-app removal (member of a SYNC group)
Open BudgeTrak → Settings → SYNC → **Leave Group**. Your device is marked as removed in the group's device roster, your real-time presence record is deleted, and your device's encryption keys to the group are wiped. The shared data itself stays in the group for the remaining members; if you want the entire group deleted, the admin must dissolve it.

### 3. Local-only deletion
Uninstalling BudgeTrak removes all on-device data immediately (transactions, settings, receipt photos, encrypted backups stored in the app's private folder). If you only used BudgeTrak in solo mode (no SYNC), no cloud-side data ever existed and uninstall fully completes the deletion.

### 4. Automatic deletion
SYNC groups that have not been opened by any member device for 90 consecutive days are automatically and permanently deleted by a server-side cleanup process. This includes all transactions, encrypted photos, and metadata. There is no recovery from this automatic cleanup; ensure you have a local backup before letting a group go inactive.

### Why we do not offer manual deletion by email
BudgeTrak deliberately does not associate your cloud data with your name, email address, or any identifier we could use to look up "your" records on request. Anonymous authentication, end-to-end encryption, and randomly-generated group identifiers are what make the privacy guarantees in this policy possible — but the same design means that if you email asking us to delete a specific group, we have no way to verify the group is yours or even to locate it among the encrypted blobs on our servers.

If you have lost access to your device or to a group whose admin you can no longer reach, the 90-day inactivity cleanup above is the deletion mechanism. Make sure you have a local backup of any data you would like to keep before that window expires.

What deletion does **not** affect: anonymous crash records (retained by the crash reporting provider for 90 days per their standard policy regardless of in-app actions), and advertising identifiers (managed by Android at the device level — reset via your device settings).

## Data Retention

- **On-device data** is retained until you delete it or uninstall the app.
- **SYNC cloud data** is automatically deleted 90 days after the last activity on a group, and immediately deleted when a group is dissolved.
- **Help Chat transcripts** are stored anonymously and automatically deleted **7 days** after the last update by a server-side time-to-live policy. Local copies on your device are pruned after 48 hours regardless.
- **Crash reports** are retained by the crash reporting provider according to their standard retention policies (currently 90 days for crash data).
- **Receipt photos in cloud storage** follow the retention period your group admin sets in Settings, or are kept indefinitely if no retention period is configured. They are immediately deleted when you remove the corresponding transaction or photo.

## Children's Privacy

BudgeTrak is a personal finance tool intended for users aged 13 and over. We do not knowingly collect personal information from children under 13. If you believe a child under 13 has provided us with personal information, please contact us at **support@techadvantageapps.com** and we will take steps to delete it.

## International Users

BudgeTrak is published from the United States. If you use the app from outside the United States, please be aware that any data you choose to sync to the cloud (which is encrypted before it leaves your device) may be relayed through servers operated by our third-party processors in the United States or other countries where they maintain infrastructure. By using BudgeTrak's SYNC feature, you consent to this relay.

## Changes to This Policy

We may update this privacy policy from time to time, particularly when we add or remove features that affect what data is collected. When we make material changes, we will update the "Last updated" date at the top of this page and, where appropriate, notify you within the app. Your continued use of BudgeTrak after a policy update constitutes acceptance of the revised policy.

## Contact Us

If you have questions about this privacy policy or BudgeTrak's data practices, please contact:

**Tech Advantage LLC**
Email: **support@techadvantageapps.com**

We will respond to legitimate privacy inquiries within a reasonable time, typically within 30 days.
