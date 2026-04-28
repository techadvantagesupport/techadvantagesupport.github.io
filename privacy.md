# BudgeTrak Privacy Policy

**Effective date:** April 11, 2026
**Last updated:** April 11, 2026

## Plain-English Summary

BudgeTrak is a personal budgeting app. Your financial data lives on your device. If you choose to enable the SYNC feature to share your budget across multiple devices in your household, that data is end-to-end encrypted before it leaves your device — neither we nor any cloud provider can read your transactions, balances, or merchant names. We do not sell your data, we do not show it to advertisers, and we do not analyze it to build a profile of you. The full policy below explains exactly what is collected, where it goes, and how to delete it.

## Who We Are

BudgeTrak is published by **Tech Advantage LLC** ("we", "us", "our"). You can contact us at **techadvantagesupport@gmail.com** for any privacy-related questions or requests.

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
- Only the encrypted data is uploaded to Google Firebase (Firestore, Cloud Storage, and Realtime Database) for relay to other devices in your group.
- The encryption key never leaves your devices. Google, our servers, and any third party with access to the cloud storage **cannot** decrypt your financial data — they can only see encrypted blobs.
- Each linked device decrypts the data locally using the shared key.

When you leave a SYNC group or dissolve it, your local data is preserved on your device but the cloud copy is deleted (with a 90-day cleanup window for orphan data).

### Diagnostic and Crash Data

To keep BudgeTrak stable and identify bugs, we use **Google Firebase Crashlytics** to collect crash reports and basic diagnostic information. This collection is **on by default** but can be turned off at any time in **Settings → Privacy → Send crash reports**.

When crash reporting is enabled, the data we collect includes:

- Crash stack traces and error messages.
- Anonymous device information (model, OS version, app version).
- An anonymous Firebase Authentication user ID (if you use SYNC) — this is a random identifier, not your name or email.
- Diagnostic counters: the number of transactions, recurring expenses, and period-ledger entries you have; sync status (`healthy`, `dead`, or `off`); the number of devices in your SYNC group; and the date of your last period refresh.
- A **one-way hash digest** of your available cash balance (computed locally as a hex digest before being sent). The actual cash value never leaves your device, and the hash cannot be reversed to recover the original number.
- Timestamped lifecycle events like "listener started," "token refreshed," or "period boundary crossed" used to debug sync issues.

Crash data does **not** include any of the following: the contents of your transactions, merchant names, amounts, dates, descriptions, categories, receipt photos, encryption keys, or any other personal financial information. We hash the only piece of financial data that touches Crashlytics (your cash balance) precisely so that even we cannot read it.

If you disable crash reporting, none of the above is collected — and the daily diagnostic snapshot we use to confirm devices are healthy is also skipped. We recommend leaving it on so we can detect and fix bugs that affect real users, but the choice is yours.

### Authentication and Anti-Abuse

If you use SYNC, BudgeTrak signs you in to Firebase using **anonymous authentication** (no email or password required). Your device is also verified using **Google Play Integrity (App Check)** to prevent unauthorized clients from accessing the cloud relay. Neither of these systems collects personal information about you.

### Subscription and Purchase Data

If you upgrade to a paid tier or subscribe to BudgeTrak Premium, the purchase is processed entirely by **Google Play Billing**. We do not see your payment method, credit card number, or billing address — Google handles all of that. We only receive a confirmation that your purchase is valid, used to unlock the corresponding features in the app.

### Advertising (Free Tier Only)

The free tier of BudgeTrak displays banner ads served by **Google AdMob**. AdMob may collect a limited advertising identifier and basic device information to serve ads, subject to Google's own privacy policy. You can reset or limit your advertising identifier in your Android device settings at any time. If you upgrade to a paid tier or subscribe to Premium, ads are removed and AdMob is no longer loaded.

### What We Do **Not** Collect

We want to be specific about this. BudgeTrak does **not** collect:

- Your name, email address, phone number, or any other directly identifying personal information.
- Your physical location, GPS coordinates, or IP address (beyond what Google services receive automatically for routing).
- Your contacts, calendar, photos library (other than receipt photos you explicitly attach), call history, SMS messages, or browsing history.
- Your bank account credentials, routing numbers, or login details for any financial institution.
- Any health, fitness, or biometric data.

## How We Use Information

We use the limited information we collect for exactly these purposes, and nothing else:

- **To provide the app's core functionality** (calculate your budget, sync data across your devices if you opted in, display your transactions).
- **To diagnose crashes and bugs** so we can fix them in the next release.
- **To verify the integrity of your subscription** if you have upgraded.
- **To serve ads** on the free tier via AdMob.

We do **not**:

- Sell your data to anyone, ever, for any purpose.
- Share your data with data brokers, marketing networks, or analytics companies (other than the Google services listed above).
- Use your financial data to train machine learning models or AI systems.
- Build a profile of you for advertising or any other purpose.

## How We Protect Your Information

- **End-to-end encryption** for all SYNC data using ChaCha20-Poly1305, with the encryption key generated and stored only on your devices.
- **Encrypted at rest** in cloud storage — even Google's servers only ever see ciphertext.
- **Encrypted in transit** using HTTPS / TLS for all network communication.
- **App Check** verification using Google Play Integrity to block unauthorized clients from accessing the SYNC backend.
- **Optional password-encrypted backups** using PBKDF2 key derivation if you enable backup encryption in Settings.
- **No server-side decryption capability** — by design, we cannot read your data even if we wanted to or were compelled to.

No system is perfectly secure, but we follow industry best practices and have designed BudgeTrak to minimize what we ever have access to.

## Third-Party Services

BudgeTrak relies on the following third-party services. Each has its own privacy policy that governs how they handle the limited data we share with them.

| Service | Purpose | What it sees |
|---|---|---|
| **Google Firebase Firestore** | Encrypted SYNC data relay | Encrypted blobs only |
| **Google Firebase Cloud Storage** | Encrypted receipt photo storage (SYNC) | Encrypted blobs only |
| **Google Firebase Realtime Database** | Device presence (online/offline) | Anonymous device IDs |
| **Google Firebase Authentication** | Anonymous sign-in for SYNC | Anonymous user token |
| **Google Firebase App Check** | Anti-abuse verification | Play Integrity attestation |
| **Google Firebase Crashlytics** | Crash reports and diagnostics | Crash data, no financial data |
| **Google Gemini** (opt-in AI features only) | Receipt reading; CSV transaction categorization | Receipt image contents; merchant, amount, date of imported bank transactions |
| **Google Play Billing** | Subscription and one-time purchases | Payment info (handled entirely by Google) |
| **Google AdMob** (free tier only) | Banner advertising | Advertising ID, basic device info |

You can review Google's privacy practices at [https://policies.google.com/privacy](https://policies.google.com/privacy).

## AI-Assisted Features (Opt-In, Paid and Subscriber Tiers)

BudgeTrak offers two optional AI-assisted features powered by Google's Gemini models, accessed through Firebase AI Logic.

### AI Receipt Scanning (Subscribers)
When a subscriber taps the sparkle icon in the transaction dialog, BudgeTrak sends the receipt photo to Google Gemini to extract the merchant, date, amount, and category. The response is returned directly to your device and stored only in your transaction record.

### AI CSV Categorization (Paid and Subscriber tiers, off by default)
When enabled in Settings, BudgeTrak sends the merchant name, amount, and date of newly-imported bank transactions to Google Gemini to choose the best-matching category for each one. Only transactions that BudgeTrak's on-device categorizer cannot confidently classify are sent.

### What's never sent to the AI provider
- Your account balances or totals
- Your historical transactions (other than the specific imported rows or receipt being processed)
- Your encryption keys, device identifiers, or authentication tokens
- Your receipt photos (they are only sent by Receipt Scanning above, never by CSV Categorization)

### How your data is protected
- All requests are encrypted in transit (HTTPS/TLS).
- Google deletes request and response data once the request completes; nothing is stored on Google's servers for these features.
- Per Firebase AI Logic's default configuration, **your data is not used to train Google's models**.
- Both features can be disabled in Settings at any time, which falls back to BudgeTrak's fully on-device behavior.

Free-tier users have no access to either AI feature, and no data from Free-tier accounts is ever sent to the AI provider.

## Your Rights and Choices

You have full control over your data in BudgeTrak.

- **Delete everything**: Uninstalling BudgeTrak removes all locally stored data from your device. If you also use SYNC, leave or dissolve your SYNC group from the SYNC screen first to remove the cloud copy.
- **Leave a SYNC group**: Tap "Leave Group" on the SYNC screen. Your local data is preserved; cloud data tied to your device is removed.
- **Dissolve a SYNC group** (admin only): Tap "Dissolve Group" on the SYNC screen. All cloud data for the group is permanently deleted; each device retains its local copy.
- **Export your data**: Use the Save feature on the Transactions screen to export your transactions in CSV, Excel, or PDF format. Backups via Settings include all your budget data in a single file.
- **Disable crash reporting**: Open **Settings → Privacy → Send crash reports** in BudgeTrak and uncheck the box. The change takes effect immediately, the daily diagnostic snapshot stops, and Firebase Crashlytics is told to stop collecting any data from your device.
- **Limit ad tracking**: Reset or limit your advertising identifier in your Android device settings under Privacy → Ads.

If you want us to confirm what data we hold about you (note: in nearly all cases, the answer is "nothing personally identifying") or have any other privacy request, contact us at **techadvantagesupport@gmail.com**.

## Data Retention

- **On-device data** is retained until you delete it or uninstall the app.
- **SYNC cloud data** is automatically deleted 90 days after the last activity on a group, and immediately deleted when a group is dissolved.
- **Crash reports** are retained by Google Firebase Crashlytics according to Google's standard retention policies (currently 90 days for crash data).
- **Receipt photos in cloud storage** follow the retention period your group admin sets in Settings, or are kept indefinitely if no retention period is configured. They are immediately deleted when you remove the corresponding transaction or photo.

## Children's Privacy

BudgeTrak is a personal finance tool intended for users aged 13 and over. We do not knowingly collect personal information from children under 13. If you believe a child under 13 has provided us with personal information, please contact us at **techadvantagesupport@gmail.com** and we will take steps to delete it.

## International Users

BudgeTrak is published from the United States. If you use the app from outside the United States, please be aware that any data you choose to sync to the cloud (which is encrypted before it leaves your device) may be relayed through servers operated by Google in the United States or other countries where Google maintains infrastructure. By using BudgeTrak's SYNC feature, you consent to this relay.

## Changes to This Policy

We may update this privacy policy from time to time, particularly when we add or remove features that affect what data is collected. When we make material changes, we will update the "Last updated" date at the top of this page and, where appropriate, notify you within the app. Your continued use of BudgeTrak after a policy update constitutes acceptance of the revised policy.

## Contact Us

If you have questions about this privacy policy or BudgeTrak's data practices, please contact:

**Tech Advantage LLC**
Email: **techadvantagesupport@gmail.com**

We will respond to legitimate privacy inquiries within a reasonable time, typically within 30 days.
