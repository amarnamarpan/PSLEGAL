#!/usr/bin/python3

#
#  Copyright 2019-2021 Arpan Mandal
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from __future__ import division
import string
import math
import timeit
import sys
start_time = timeit.default_timer()
import numpy as np


leg_terms = [
'ADR',
'Ab initio',
'Abandonment',
'Abatement',
'Abduction',
'Abovementioned',
'Abscond',
'Absolute',
'Absolute discharge',
'Absolute owner',
'Absolute privilege',
'Abstract of title',
'Abuse of process',
'Abuttals',
'Acceptance',
'Acceptance of service',
'Acceptor',
'Accessory',
'Accomplice',
'Accord and Satisfaction',
'Accordingly',
'Accounts',
'Accumulation',
'Accused',
'Acknowledgement',
'Acknowledgement of Service',
'Acquiescence',
'Acquit',
'Acquittal',
'Act of God',
'Act of bankruptcy',
'Action',
'Active trust',
'Actual bodily harm',
'Actual loss',
'Actuary',
'Actus reus',
'Ad hoc',
'Ad idem',
'Ad infinitum',
'Ad valorem',
'Additional voluntary contribution',
'Ademption',
'Adjourned sine die',
'Adjournment',
'Adjudgeadjudicate',
'Adjudication order',
'Administration order',
'Administrative law',
'Administrator',
'Admissibility of Evidence',
'Admission',
'Admonition',
'Adoption',
'Adoptive child',
'Adoptive parent',
'Adverse possession',
'Adverse witness',
'Advocate',
'Affidavit',
'Affirm',
'Affirmation',
'Affray',
'Aforementioned',
'Aforesaid',
'Age of consent',
'Agency',
'Agent',
'Aggravated assault',
'Aggravated burglary',
'Aggravated damages',
'Aggravated vehicle taking',
'Agricultural holding',
'Aiding and abetting',
'Airspace',
'Alias',
'Alibi',
'Alien',
'Alienation',
'All and sundry',
'All that',
'Allegation',
'Alleviate',
'Allocation rate',
'Allotment',
'Alternate director',
'Alternative dispute resolution',
'Alternative verdict',
'Amalgamation',
'Ambiguity',
'Ambulatory will',
'Amnesty',
'Ancient lights',
'Annual accounts',
'Annual general Meeting',
'Annual return',
'Annuitant',
'Annuity',
'Annul',
'Ante',
'Antecedents',
'Antedate',
'Antenuptial agreement',
'Anton Piller order',
'Appeal',
'Appeals',
'Appearance',
'Appellant',
'Appellate',
'Appellate jurisdiction',
'Appertaining to Applicant',
'Appointee',
'Appointor',
'Appurtenances',
'Arbitrage',
'Arbitration',
'Arbitrator',
'Arraignment',
'Arrears',
'Arrest',
'Arrestable offence',
'Arson',
'Articles',
'Articles of association',
'Assault',
'Assent',
'Asset',
'Assign',
'Assignment',
'Assurance',
'Assure',
'Assured',
'Assured shorthold Tenancy',
'Attachment and committal',
'Attachment of earnings',
'Attest',
'Attorney',
'Attorney General',
'Audi alteram partem',
'Audit',
'Auditors report',
'Authorised Investments',
'Authorised share Capital',
'Autopsy',
'Backlog',
'Bail',
'Bail hostel',
'Bailee',
'Bailiff',
'Bailiwick',
'Bailment',
'Bailor',
'Balance sheet',
'Bankers draft',
'Bankrupt',
'Bankruptcy order',
'Bankruptcy search',
'Bar',
'Bare trust',
'Bare trustee',
'Bargain and sale',
'Barrister',
'Barter',
'Battery',
'Bearer',
'Bench',
'Bench warrant',
'Beneficial interest',
'Beneficial owner',
'Beneficiary',
'Bequeath',
'Bequest',
'Bigamy',
'Bill of costs',
'Bill of exchange',
'Bill of lading',
'Bill of sale',
'Binding effect',
'Binding over',
'Binding precedent',
'Blackmail',
'Bodily harm',
'Bona fide',
'Bona vacantia',
'Bond',
'Bonded goods',
'Breach of contract',
'Burden of proof',
'Call',
'Calledup capital',
'Canon law',
'Capacity',
'Capital allowances',
'Capital gain',
'Capital gains tax',
'Capital punishment',
'Capital redemption reserve',
'Care order',
'Careless driving',
'Cartel',
'Case Number',
'Case Status',
'Case law',
'Case stated',
'Causation',
'Cause List',
'Cause of Action',
'Cause of action',
'Causing death by careless and inconsiderate driving',
'Causing death by dangerous driving',
'Caution',
'Caveat',
'Caveat emptor',
'Central Criminal Court',
'Certificate of Incorporation',
'Certificate of origin',
'Certiorari',
'Challenge for cause',
'Challenge to a jury',
'Challenge to the array',
'Challenge without Cause',
'Chambers',
'Chancery Division',
'Charge',
'Charge certificate',
'Charge sheet',
'Chargeable event',
'Chargeable gain',
'Charges clause',
'Charges register',
'Charging clause',
'Charging order',
'Charity',
'Charity Commission',
'Chattel',
'Chattels',
'Chattels personal',
'Chattels real',
'Cheat',
'Cheque',
'Cheque card',
'Chief rent',
'Child',
'Child Support Agency',
'Child Support Maintenance',
'Child abuse',
'Child assessment Order',
'Children in care',
'Chose',
'Chose in action',
'Chose in possession',
'Circuit',
'Circuit Court',
'Circuit Judge',
'Circuit judge',
'Circumstantial evidence',
'Citation',
'Citizens arrest',
'Civil',
'Civil Procedure Code',
'Civil court',
'Claim',
'Claimant',
'Class action',
'Clause',
'Clayton’s Case',
'Clearing bank',
'Clerk to the Justices',
'Close company',
'Closing order',
'Codicil',
'Codifying statute',
'Coercion',
'Collateral',
'Collusion',
'Commissioner for Oaths',
'Commissions',
'Committal for sentence',
'Committal for trial',
'Committal order',
'Committal proceedings',
'Committee of Inspection',
'Common assault',
'Common duty of care',
'Common law',
'Common seal',
'Commorientes',
'Community service order',
'Companies House',
'Company',
'Company secretary',
'Compensation',
'Compensation for loss of office',
'Compensation order',
'Complaint',
'Completion',
'Composition with Creditors',
'Compulsory purchase',
'Compulsory winding up',
'Concealment',
'Concealment of securities',
'Conclusive evidence',
'Concurrent sentence',
'Condition',
'Condition precedent',
'Condition subsequent',
'Conditional agreement',
'Conditional discharge',
'Conditional sale agreement',
'Confiscation order',
'Consecutive sentence',
'Consent',
'Consent order',
'Consideration',
'Consign',
'Consignee',
'Consignor',
'Consistory Court',
'Conspiracy',
'Construction',
'Constructive',
'Constructive dismissal',
'Constructive notice',
'Constructive trust',
'Consumer credit agreement',
'Contempt',
'Contempt of court',
'Contemptuous damages',
'Contingency fee',
'Contingent legacy',
'Contract',
'Contract for services',
'Contract law',
'Contract of exchange',
'Contract of service',
'Contributory negligence',
'Conversion',
'Convey',
'Conveyance',
'Conveyancing',
'Conviction',
'Copyright',
'Coroner',
'Corporate body',
'Corporation',
'Corporation tax',
'Corpus',
'Corpus delicti',
'Costs',
'Counsel',
'Counterclaim',
'Counterfeit',
'Counterpart',
'County court',
'County court judge',
'Coupon',
'Court Hall',
'Court of Appeal',
'Court of Protection',
'Covenant',
'Creditor',
'Creditors voluntary winding up',
'Crime',
'Criminal',
'Criminal Procedure Code.',
'Criminal damage',
'Criminal responsibility',
'Cross-examination',
'Crossexamine',
'Crown Court',
'Culpa',
'Cum dividend',
'Cumulative preference shares',
'Curfew',
'Curtilage',
'Customs duties',
'Damages',
'Dangerous driving',
'Date of Hearing',
'Date of Institution',
'De facto',
'De jure',
'De minimis non curat lex',
'De novo',
'Debenture',
'Debt Debtor',
'Debt securities',
'Debtor',
'Deceit',
'Decree',
'Decree absolute',
'Decree nisi',
'Deed',
'Deed of arrangement',
'Defamation',
'Default',
'Defence',
'Defendant',
'Delay',
'Delegatus non potest delegare',
'Dependant',
'Deponent',
'Deposition',
'Depreciation',
'Derogation',
'Descendant',
'Determination',
'Detinue',
'Devise',
'Devise Devisee',
'Diminished responsibility',
'Diocese',
'Diplomatic immunity',
'Directiondirecting',
'Director',
'Director of Public Prosecutions',
'Disbursement',
'Discharge',
'Disclaimdisclaimer',
'Discovery',
'Discretionary trust',
'Disposal',
'Dispute',
'Distraindistress',
'Distraint',
'District',
'District Court',
'District Judge',
'Dividend',
'Divorce',
'Divorce petition',
'Domicile',
'Domicile of choice',
'Domicile of origin',
'Domiciled',
'Dominant tenement',
'Donatio mortis causa',
'Donee',
'Donor',
'Drawee',
'Drawer',
'Duces tecum',
'Duress',
'Duty',
'Easement',
'Emolument',
'Enabling legislation',
'Endorsement',
'Endorsement of claim',
'Endowment',
'Endowment policy',
'Enduring power of Attorney',
'Engrossment',
'Equitable mortgage',
'Equity',
'Escrow',
'Estate',
'Estimate',
'Estoppel',
'Et seq',
'Euthanasia',
'Evidence',
'Ex aequo et bono',
'Ex gratia',
'Ex parte',
'Ex post facto',
'Ex turpi causa non oritur actio',
'Ex works',
'Examination-in-chief',
'Excess of jurisdiction',
'Exchange of contract',
'Excise duty',
'Exclusions',
'Exclusive licence Ex dividend',
'Execute',
'Executed',
'Executive',
'Executive director',
'Executor',
'Executory',
'Executrix',
'Exemplary damages',
'Exhibit',
'Expert witness',
'Express trust',
'Extradition',
'Extraordinary Resolution',
'Extraordinary general Meeting',
'Factor',
'False imprisonment',
'False pretence',
'False representation',
'Family Division',
'Fee simple',
'Fee tail',
'Felony',
'Feme covert',
'Feme sole',
'Feu',
'Feu duty',
'Fiduciary',
'Fieri facias',
'Final judgement',
'Fitness to plead',
'Fixed charge',
'Floating charge',
'Forbearance',
'Force majeure',
'Foreclosure',
'Forfeiture',
'Fostering',
'Fraud',
'Fraudulent conveyance',
'Fraudulent preference',
'Fraudulent trading',
'Free of encumbrances',
'Freehold',
'Freeholder',
'Frustration',
'Fundamental Rights',
'Futures contract',
'Garnishee',
'Garnishee order',
'General damages',
'General meeting',
'Goodwill',
'Gram Nyayalas',
'Grant',
'Grant of probate',
'Grievous bodily harm',
'Gross negligence',
'Guarantee',
'Guarantee company',
'Guarantor',
'Guardian',
'Guilty',
'HM Customs and Excise',
'HM Land Registry',
'Habeas Corpus',
'Habeas corpus',
'Harassment of Occupiers',
'Harassment of debtors',
'Hearsay',
'Hearsay evidence',
'Hereditament',
'High Court',
'High Court of Justice',
'Hire',
'Hire purchase',
'Holding company',
'Hostile witness',
'House of Lords',
'Housing associations',
'Hypothecation',
'IOU',
'In pari delicto',
'In personam',
'In rem',
'Incorporeal',
'Incorporeal hereditament',
'Indian Penal Code',
'Indict',
'Indictable offence',
'Indictment',
'Injunction',
'Insolvent',
'Intangible property',
'Inter alia',
'Inter partes',
'Inter vivos',
'Interest',
'Interim order',
'Interlineation',
'Interlocutory Judgement',
'Interlocutory Proceedings',
'Interlocutory injunction',
'Interpretation',
'Interrogatories',
'Intestacyintestate',
'Intestate',
'Intimidation',
'Invitation to treat',
'Involuntary manslaughter',
'Issue',
'Issued share capital',
'Issues',
'Joint and several liability',
'Joint lives policy',
'Joint tenancy',
'Joint will',
'Joyriding',
'Judge',
'Judge Advocate General',
'Judge Advocate Generals',
'Judge Advocate of the Fleet',
'Judge advocate',
'Judge in chambers',
'Judgement',
'Judgement creditor',
'Judgement debtor',
'Judgement in default',
'Judgement summons',
'Judicial discretion',
'Judicial immunity',
'Judicial precedent',
'Judicial review',
'Judicial separation',
'Judiciary',
'Junior barrister',
'Junior counsel',
'Jurisdiction',
'Juror',
'Jury',
'Jury service',
'Just and equitable winding up',
'Justice of the Peace',
'Justification',
'Justifying bail',
'Juvenile offender',
'Kerb crawling',
'Kidnap',
'Kin',
'King’s Inns',
'Knock for knock',
'Knock-for-knock',
'Knowhow',
'Laches',
'Land',
'Landlord',
'Lasting powers of attorney',
'Lawsuit',
'Lawyer',
'Lay litigant',
'Leading question',
'Lease',
'Leasehold',
'Legacy',
'Legal Aid',
'Legal aid scheme',
'Legal professional privilege',
'Legatee',
'Legislative Assembly',
'Legislature',
'Lessee',
'Lessor',
'Letter of credit',
'Letters of administration',
'Liabilities',
'Liability',
'Libel',
'Licence',
'Licensed conveyancer',
'Licensee',
'Lien',
'Life assurance policy',
'Life assured',
'Life estate',
'Life imprisonment',
'Life interest',
'Life tenant',
'Limitation of actions',
'Limited company',
'Lineal descendant',
'Liquidated damages',
'Liquidation',
'Liquidator',
'Lis pendens',
'Litigant',
'Litigation',
'Loan capital',
'Loan creditor',
'Locus standi',
'Lok Adalats',
'Magistrate',
'Magistrates court',
'Maintenance',
'Majority',
'Male issue',
'Malfeasance',
'Malice',
'Malice aforethought',
'Malicious falsehood',
'Malicious prosecution',
'Mandamus',
'Mandate',
'Manslaughter',
'Market overt',
'Martial law',
'Master of the Rolls',
'Material facts',
'Matricide',
'Matrimonial causes',
'Matrimonial home',
'Mediation',
'Memorandum and articles of association',
'Mens rea',
'Mercantile law',
'Merchantable quality',
'Mesne profits',
'Messuage',
'Minor',
'Minority',
'Minutes',
'Misadventure',
'Miscarriage of justice',
'Misconduct',
'Misdirection',
'Misfeasance',
'Misjoinder',
'Misrepresentation',
'Mistrial',
'Mitigation',
'Mitigation of damages',
'Moiety',
'MolestMolestation',
'Money laundering',
'Moratorium',
'Mortgage',
'Mortgagee',
'Mortgagor',
'Motive',
'Muniments',
'Naked trust',
'Natural justice',
'Natural person',
'Naturalisation',
'Negligence',
'Negligent',
'Negotiable instrument',
'Nemo judex in sua causa',
'Next of kin',
'Non est factum',
'Non-joinder',
'Nondisclosure',
'Nonexclusive licence',
'Nonfeasance',
'Not guilty',
'Not negotiable',
'Notary',
'Notice',
'Notice to quit',
'Novation',
'Nudum pactum',
'Nuisance',
'Oath',
'Obiter dicta',
'Objects clause',
'Obligation',
'Obligee',
'Obligor',
'Obstruction',
'Occupation',
'Occupational pension Scheme',
'Occupier',
'Offensive weapon',
'Offer',
'Offeree Offeror',
'Official Solicitor',
'Official receiver',
'Official secret',
'Omission',
'Oppression',
'Option',
'Order',
'Order in Council',
'Orders',
'Original Jurisdiction',
'Originating summons',
'Out-of-court settlement',
'Outlaw',
'Overt act',
'Panel',
'Pardon',
'Pari passu',
'Parole',
'Partition',
'Partnership',
'Party',
'Passing off',
'Patent',
'Patricide',
'Pawn',
'Payee',
'Payment into court',
'Payor',
'Penalty',
'Penalty points',
'Pendency',
'Pendente lite',
'Per',
'Per pro',
'Per quod',
'Per quod servitium amisit',
'Per se',
'Per stirpes',
'Performance',
'Perjury',
'Perpetuity',
'Personal guarantee',
'Personal injury',
'Personal property',
'Personal representative',
'Personalty',
'Personation',
'Perverting the course of justice',
'Petition',
'Petitioner',
'Picket',
'Plaint',
'Plaintiff',
'Plea',
'Plea bargain',
'Plead',
'Pleadings',
'Pledge',
'Plenipotentiary',
'Poaching',
'Polygamy',
'Possess',
'Possession',
'Possessory title',
'Postmortem',
'Power of appointment',
'Power of attorney',
'Practising certificate',
'Prayer',
'Preamble',
'Precatory words',
'Precedent',
'Precedents',
'Precept',
'Preemption',
'Preference',
'Preference shares',
'Preferential creditor',
'Prescription',
'Prima facie',
'Principal',
'Private law',
'Privilege',
'Privity of contract',
'Privy Council',
'Privy Purse',
'Pro rata',
'Pro tempore',
'Probate',
'Probate Registry',
'Probate law',
'Probation',
'Procedural',
'Process',
'Procurator',
'Procurator fiscal',
'Product liability',
'Profit à prendre',
'Prohibition',
'Promisee Promisor',
'Promissory note',
'Property',
'Prosecution',
'Prosecutor',
'Prospectus',
'Prostitution',
'Protected tenancy',
'Proviso',
'Provocation',
'Proxy',
'Proxy form',
'Public mischief',
'Public nuisance',
'Punitive damages',
'Putative father',
'Qualifying child',
'Quango',
'Quantum',
'Quantum meruit',
'Quarter days',
'Queens Bench Division',
'Queens Counsel',
'Queens evidence',
'Quid pro quo',
'Quiet enjoyment',
'Quiet possession',
'Quo Warranto',
'Quo warranto',
'Quorum',
'Racial discrimination',
'Rack rent',
'Rape',
'Real',
'Real estate',
'Real property',
'Realty',
'Reasonable force',
'Rebuttable presumption',
'Receiver',
'Receiving',
'Recognisance',
'Record',
'Recorder',
'Recovery',
'Redemption',
'Redundancy',
'Registered land',
'Registered office',
'Registrar of Companies',
'Registry',
'Registry offices',
'Reinsurance',
'Release',
'Remainder',
'Remand',
'Remedy',
'Renouncing probate',
'Rent',
'Repeat offender',
'Replevin',
'Reply',
'Repossess',
'Repossession',
'Representation',
'Representative action',
'Reprieve Rescission',
'Res ipsa loquitur',
'Rescission',
'Reservation of title',
'Reserved costs',
'Reserved judgment',
'Reserves',
'Residence',
'Residence order',
'Residuary legacy',
'Residue',
'Resisting arrest',
'Resolution',
'Respondent',
'Restitutio in integrum',
'Restitution',
'Restraining order',
'Restriction',
'Restriction order',
'Restrictive covenant',
'Resulting trust',
'Retainer',
'Retention of title',
'Reversion',
'Reversion Revocation',
'Review',
'Revoke',
'Revolving credit Agreement',
'Right of way',
'Rights issue',
'Riot',
'Riparian rights',
'Robbery',
'SWIFT payment',
'Sale or return',
'Salvage',
'Sanction',
'Satisfaction',
'Scheme of Arrangement',
'Scienter',
'Scrip',
'Scrip dividend',
'Scrip issue',
'Search',
'Search warrant',
'Securities',
'Security',
'Security of tenure',
'Sedition',
'Senior counsel',
'Sentence',
'Separation of Powers',
'Separation order',
'Sequestration',
'Service',
'Servient tenement',
'Settle',
'Settlement',
'Settlor',
'Several',
'Shadow director',
'Share',
'Share capital',
'Share certificate',
'Share premium Account',
'Sheriff',
'Shoplifting',
'Shorthold tenancy',
'Silent partner',
'Sine die',
'Slander',
'Slander of title',
'Small claims court',
'Smuggling',
'Sold note',
'Soliciting',
'Solicitor',
'Solicitor General',
'Special Courts',
'Special Criminal Court',
'Special resolution',
'Specific performance',
'Spent conviction',
'Squatter',
'Stage of the Case',
'Stalking',
'Stamp duty',
'Stare decisis',
'Statement of claim',
'Status',
'Statute',
'Statute book',
'Statute law',
'Statute of limitation',
'Statutory accounts',
'Statutory audit',
'Statutory books',
'Statutory demand',
'Statutory instrument',
'Stay of execution',
'Stipendiary magistrate',
'Stockbroker',
'Strict liability',
'Sub judice',
'Subduct',
'Subject to contract',
'Subpoena',
'Subrogation',
'Subscribers',
'Subsidiarity',
'Subsidiary',
'Substantive',
'Substituted service',
'Successor',
'Sue',
'Sui generis',
'Sui juris',
'Suicide',
'Suit',
'Summary judgement',
'Summary offence',
'Summary proceedings',
'Summary trial',
'Summing up',
'Summons',
'Superior courts',
'Supervision order',
'Supra',
'Supreme Court',
'Surcharge',
'Surety',
'Suspended sentence',
'Tangible asset',
'Tangible property',
'Tax',
'Tax avoidance',
'Tax evasion',
'Tax point',
'Taxable supply',
'Taxation',
'Taxation of costs',
'Teeming and lading',
'Tenancy in common',
'Tenant',
'Tender',
'Tenement',
'Tenure',
'Term',
'Terra',
'Terrorism',
'Testament',
'Testamentum',
'Testator',
'Testify',
'Testimony',
'Theft',
'Threatening behaviour',
'Timeshare',
'Title',
'Title deeds',
'Toll',
'Tort',
'Tortfeasor',
'Tracing',
'Trademark',
'Transcript',
'Transferable securities',
'Transferee',
'Transferor',
'Treason',
'Treasure trove',
'Treasury',
'Treasury Solicitor',
'Treasury bill',
'Trespass',
'Trespassing',
'Trial',
'Tribunal',
'Tribunals',
'Trust',
'Trust corporation',
'Trust deed',
'Trustee',
'Trustee in bankruptcy',
'Uberrimae fidei',
'Ultra vires',
'Underlease',
'Undertaking',
'Undue influence',
'Unfair contract terms',
'Unfair dismissal',
'Unit trust',
'Unjust enrichment',
'Unlawful wounding',
'Unliquidated damages',
'Unreasonable behaviour',
'Unregistered company',
'Unregistered land',
'Unsecured creditor',
'Usury',
'Uterine',
'Vakalathnama',
'Variation',
'Vendee',
'Vendor',
'Verdict',
'Vesting order',
'Vexatious litigant',
'Vicarious liability',
'Videlicet',
'Violent disorder',
'Void',
'Voidable',
'Voire dire',
'Volenti non fit injuria',
'Voluntary arrangement',
'Voluntary manslaughter',
'Waiver',
'Ward of court Warrant',
'Warranty',
'Waste',
'Wayleave',
'Will',
'Winding up',
'Without prejudice',
'Witness',
'Words of art',
'Words of limitation',
'Words of purchase',
'Writ',
'Writ of execution',
'Writ of summons',
'Writs',
'Wrongful dismissal',
'Wrongful trading',
'Xoanon',
'Year',
'Young person',
'Zero hours'
]

leg_terms = [tr.lower() for tr in leg_terms]
cf_start_time = timeit.default_timer()

import os
import tokenize as sentencify
import extract_noun_phrases as npe

class PSlegalVectorizer:

    def __init__(self, version=2):
        self.legalcf = {}
        self.legalidf = {}
        self.nonlegalcf = {}
        self.nonlegalidf = {}
        self.legaldf={}
        self.nonlegaldf={}
        self.ver = 2
        if version>2:
            self.ver = 2
            print('\n\tWarning:: version can only be either 1 or 2. \n\tContinuing with latest version 2..\n')
        elif version==1:
            self.ver=1
        self.domain_specific_importance = {}
        self.vocab=[]
        self.term_scores = {}


    def vocabulary(self):
        return self.vocab

    def term_frequency(self, term, tokenized_document, normalize=False):
        if normalize:
            return float(tokenized_document.count(term))/len(set(tokenized_document))
        return float(tokenized_document.count(term))

    def sublinear_term_frequency(self, term, tokenized_document, normalize=False):
        if normalize:
            count = tokenized_document.count(term)/len(set(tokenized_document))
        else:
            count = tokenized_document.count(term)/len(set(tokenized_document))
        if count == 0:
            return 0
        return 1 + math.log1p(count)

    def augmented_term_frequency(self, term, tokenized_document):
        max_count = max([term_frequency(t, tokenized_document) for t in tokenized_document])
        return (0.5 + ((0.5 * term_frequency(term, tokenized_document))/max_count))

    def inverse_document_frequencies(self, tokenized_documents):
        idf_start_time = timeit.default_timer()
        idf_values = {}
        all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])
        self.vocab = list(set(all_tokens_set).union(set(self.vocab)))
        vocabsize = len(all_tokens_set)
        ctr=1
        for tkn in all_tokens_set:
            sys.stdout.write('\r')
            sys.stdout.write('IDF for '+str(ctr)+' token out of '+str(vocabsize)+'   '+str((ctr*100.0)/vocabsize)[:6]+'% done  (Time elapsed = '+str(float(timeit.default_timer() - start_time)/60)[:5]+'  minutes)   (ETA = '+str((float((timeit.default_timer() - idf_start_time)/60) / ctr) * (vocabsize-ctr))[:5]+'  minutes)')
            sys.stdout.flush()
            ctr+=1
            contains_token = map(lambda doc: tkn in doc, tokenized_documents)
            idf_values[tkn] = 1 + math.log1p(len(tokenized_documents)/(sum(contains_token)))
        return idf_values

    def collection_frequencies(self, tokenized_documents, normalize=False):
        cf_start_time = timeit.default_timer()
        cf_values = {}
        n_docs = len(tokenized_documents)
        all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])
        self.vocab = list(set(all_tokens_set).union(set(self.vocab)))
        vocabsize = len(all_tokens_set)
        superset = []
        for each in tokenized_documents:
            superset.extend(each)
        del tokenized_documents
        ctr=1
        for tkn in all_tokens_set:
            sys.stdout.write('\r')
            sys.stdout.write('CF for '+str(ctr)+' token out of '+str(vocabsize)+'   '+str((ctr*100.0)/vocabsize)[:6]+'% done  (Time elapsed = '+str(float(timeit.default_timer() - start_time)/60)[:5]+'  minutes)   (ETA = '+str((float((timeit.default_timer() - cf_start_time)/60) / ctr) * (vocabsize-ctr))[:5]+'  minutes)')
            sys.stdout.flush()
            ctr+=1
            cf_values[tkn] = superset.count(tkn)
            if normalize:
                cf_values[tkn] = cf_values[tkn] / n_docs
        return cf_values

    def calculate_frequencies(self,tokenized_documents, normalize=False):
        cf_start_time = timeit.default_timer()
        cf_values = {}
        df_values = {}
        idf_values={}
        n_docs = len(tokenized_documents)
        # all_tokens_set=set([])
        # for sublist in tokenized_documents:
        #     print(type(sublist[0]),type(sublist),type(tokenized_documents))
        #     print(len(sublist[0]),len(sublist),len(tokenized_documents))
        #     all_tokens_set.union(set(sublist))
        all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])
        self.vocab = list(set(all_tokens_set).union(set(self.vocab)))
        vocabsize = len(all_tokens_set)
        for each in all_tokens_set:
            cf_values[each] = 0.0
            df_values[each] = 0.0
            idf_values[each] = 0.0
        ctr=1
        for doc in tokenized_documents:
            df_words = list(set(doc))
            for each in df_words:
                df_values[each] += 1
            for each in doc:
                cf_values[each] += 1
            sys.stdout.write('\r')
            sys.stdout.write('Calculating CF and IDF '+str((ctr*100.0)/n_docs)[:6]+'% done  (Time elapsed = '+str(float(timeit.default_timer() - start_time)/60)[:5]+'  minutes)   (ETA = '+str((float((timeit.default_timer() - cf_start_time)/60) / ctr) * (n_docs-ctr))[:5]+'  minutes)    ')
            sys.stdout.flush()
            ctr+=1
        for each in df_values:
            idf_values[each] = 1 + math.log1p(n_docs/(df_values[each]))
        if normalize:
            for each in cf_values:
                cf_values[each] = cf_values[each]/n_docs
        return (idf_values,cf_values)

    def update_frequencies(self, toks, mode='legal', normalize=False):
        self.vocab = list(set(toks).union(set(self.vocab)))
        df_words = list(set(toks))
        for each in df_words:
            if not each in self.legaldf:
                self.legaldf[each] = 0.0
            if not each in self.legalcf:
                self.legalcf[each] = 0.0
        for each in df_words:
            self.legaldf[each] += 1
        for each in toks:
            self.legalcf[each] += 1
        return

    def tfidf(self, tokenized_documents):
        tfidf_documents = []
        for document in tokenized_documents:
            doc_tfidf = []
            for term in self.legalidf.keys():
                tf = sublinear_term_frequency(term, document)
                doc_tfidf.append(tf * idf[term])
            tfidf_documents.append(doc_tfidf)
        return tfidf_documents

    def KLI(self, tokenized_documents):
        KLI_documents = []
        for document in tokenized_documents:
            doc_KLI = []
            for term in self.legalidf.keys():
                doc_KLI.append(0.0)
            doc_KLI = np.array(doc_KLI)
            for ind,term in enumerate(self.legalidf.keys()):
                tf = self.term_frequency(term, document, normalize=True)
                if tf!=0:
                    doc_KLI[ind] = tf *(math.log1p(tf / (self.legalcf[term] + 1.0)))
            KLI_documents.append(doc_KLI)
        return np.array(KLI_documents)

    def transform(self, tokenized_documents):
        kli = self.KLI(tokenized_documents)
        importance = self.domain_specific_importance
        pscore_documents = []
        row_ind=0
        for document in tokenized_documents:
            doc_pscore = []
            col_ind=0
            for term in self.legalidf.keys():
                doc_pscore.append(0.0)
            doc_pscore = np.array(doc_pscore)
            for ind,term in enumerate(self.legalidf.keys()):
                tf = self.term_frequency(term, document, normalize=True)
                if tf!=0:
                    doc_pscore[ind] = kli[row_ind][col_ind] * importance[term]
                col_ind+=1
            pscore_documents.append(doc_pscore)
            row_ind+=1
        return np.array(pscore_documents)

    def fit_doc(self, tokenized_document):
        kli = self.KLI([tokenized_document])[0]
        doc_pscore = []
        self.term_scores={}
        col_ind=0
        for term in self.legalidf.keys():
            doc_pscore.append(0.0)
        doc_pscore = np.array(doc_pscore)
        for ind,term in enumerate(self.legalidf.keys()):
            tf = self.term_frequency(term, tokenized_document, normalize=True)
            score=0
            if tf!=0:
                score = kli[ind] * self.domain_specific_importance[term]
                doc_pscore[ind] = score
            self.term_scores[term] = score
            del score
        return self.term_scores

    def get_score(self, tokenized_phrase):
        score = 0.0
        l_imp = 0.0
        phrase = ' '.join(tokenized_phrase)
        for ltr in leg_terms:
            if ltr in phrase:
                l_imp+=1
        l_imp = 1.0+math.log1p(l_imp)
        for tok in tokenized_phrase:
            if tok in self.term_scores:
                score += self.term_scores[tok]
        score = score/len(tokenized_phrase)
        return score*l_imp

    def fit(self, legal_tokenized_documents, nonlegal_tokenized_documents):
        print ('\nstarted calculating legal frequencies...')
        (self.legalidf , self.legalcf ) = self.calculate_frequencies(legal_tokenized_documents, normalize=True)
        print ('\nstarted calculating nonlegal frequencies...')
        (self.nonlegalidf , self.nonlegalcf ) = self.calculate_frequencies(nonlegal_tokenized_documents, normalize=True)

        exclusive_nonlegal_tokens = list(set(self.nonlegalcf.keys()) - set(self.legalcf.keys()))
        exclusive_legal_tokens = list(set(self.legalcf.keys())- set(self.nonlegalcf.keys()))
        for tkn in exclusive_nonlegal_tokens:
            self.legalcf[tkn]=0
            self.legalidf[tkn]=0
        for tkn in exclusive_legal_tokens:
            self.nonlegalcf[tkn]=0
            self.nonlegalidf[tkn]=0
        print ('\nstarted calculating domain_specific_importances...')
        ctr=1
        cf_start_time = timeit.default_timer()
        vocabsize = len(self.legalidf.keys())
        for term in self.legalidf.keys():
            sys.stdout.write('\r')
            sys.stdout.write('DSI for '+str(ctr)+' token out of '+str(vocabsize)+'   '+str((ctr*100.0)/vocabsize)[:6]+'% done  (Time elapsed = '+str(float(timeit.default_timer() - start_time)/60)[:5]+'  minutes)   (ETA = '+str((float((timeit.default_timer() - cf_start_time)/60) / ctr) * (vocabsize-ctr))[:5]+'  minutes)')
            sys.stdout.flush()
            ctr+=1
            if self.ver==1:
                self.domain_specific_importance[term] = (1 + math.log1p((self.legalidf[term] * self.legalcf[term]) / (self.nonlegalcf[term] * self.nonlegalidf[term] + 1)))
            elif self.ver==2:
                self.domain_specific_importance[term] = (1 + math.log1p(self.legalcf[term])*self.legalidf[term]) /   (1.0+math.log1p(self.nonlegalcf[term])*self.nonlegalidf[term])
        return

    def efficient_fit(self, legal_docs_folder, nonlegal_docs_folder,gram=1):
        # The value of gram can either be 'nnp' or some integer n representing the n-gram tokenization.
        legal_tokenized_documents = []
        nonlegal_tokenized_documents = []
        legal_flist = os.listdir(legal_docs_folder)
        nonlegal_flist = os.listdir(nonlegal_docs_folder)
        ctr=1
        sub_time = timeit.default_timer()
        for legalfn in legal_flist:
            with open(os.path.join(legal_docs_folder,legalfn), encoding="iso 8859-15") as lfp:
                text = lfp.read()
            if type(gram)==type(0):
                toks = sentencify.get_ngrams(text,gram=gram)
            elif(gram=='nnp'):
                toks = npe.extract(text)
            self.update_frequencies(toks, mode='legal', normalize=True)
            sys.stdout.write('\r')
            sys.stdout.write('Calculating legal CF and IDF '+str((ctr*100.0)/len(legal_flist))[:6]+'% done  (Time elapsed = '+str(float(timeit.default_timer() - start_time)/60)[:5]+'  minutes)   (ETA = '+str((float((timeit.default_timer() - sub_time)/60) / ctr) * (len(legal_flist)-ctr))[:5]+'  minutes)    ')
            sys.stdout.flush()
            ctr+=1
        ctr=1
        sub_time = timeit.default_timer()
        for nonlegalfn in nonlegal_flist:
            with open(os.path.join(nonlegal_docs_folder,nonlegalfn)) as lfp:
                text = lfp.read()
            if type(gram)==type(0):
                toks = sentencify.get_ngrams(text,gram=gram)
            elif(gram=='nnp'):
                toks = npe.extract(text)
            self.update_frequencies(toks, mode='nonlegal', normalize=True)
            sys.stdout.write('\r')
            sys.stdout.write('Calculating non-legal CF and IDF '+str((ctr*100.0)/len(nonlegal_flist))[:6]+'% done  (Time elapsed = '+str(float(timeit.default_timer() - start_time)/60)[:5]+'  minutes)   (ETA = '+str((float((timeit.default_timer() - sub_time)/60) / ctr) * (len(nonlegal_flist)-ctr))[:5]+'  minutes)    ')
            sys.stdout.flush()
            ctr+=1
        # print ('\nstarted calculating legal frequencies...')
        # (self.legalidf , self.legalcf ) = self.calculate_frequencies(legal_tokenized_documents, normalize=True)
        # print ('\nstarted calculating nonlegal frequencies...')
        # (self.nonlegalidf , self.nonlegalcf ) = self.calculate_frequencies(nonlegal_tokenized_documents, normalize=True)

        exclusive_nonlegal_tokens = list(set(self.nonlegalcf.keys()) - set(self.legalcf.keys()))
        exclusive_legal_tokens = list(set(self.legalcf.keys())- set(self.nonlegalcf.keys()))
        for tkn in exclusive_nonlegal_tokens:
            self.legalcf[tkn]=0
            self.legalidf[tkn]=0
            self.legaldf[tkn]=1
        for tkn in exclusive_legal_tokens:
            self.nonlegalcf[tkn]=0
            self.nonlegalidf[tkn]=0
            self.nonlegaldf[tkn]=1

        for each in self.legaldf:
            self.legalidf[each] = 1 + math.log1p(len(legal_flist)/(self.legaldf[each]))
        for each in self.nonlegaldf:
            self.nonlegalidf[each] = 1 + math.log1p(len(nonlegal_flist)/(self.nonlegaldf[each]))

        if True: # NORMALIZATION of CFs
            for each in self.legalcf:
                self.legalcf[each] = self.legalcf[each]/len(legal_flist)
            for each in self.nonlegalcf:
                self.nonlegalcf[each] = self.nonlegalcf[each]/len(nonlegal_flist)

        print ('\nstarted calculating domain_specific_importances...')
        ctr=1
        cf_start_time = timeit.default_timer()
        vocabsize = len(self.legalcf.keys())
        for term in self.legalcf.keys():
            sys.stdout.write('\r')
            sys.stdout.write('DSI for '+str(ctr)+' token out of '+str(vocabsize)+'   '+str((ctr*100.0)/vocabsize)[:6]+'% done  (Time elapsed = '+str(float(timeit.default_timer() - start_time)/60)[:5]+'  minutes)   (ETA = '+str((float((timeit.default_timer() - cf_start_time)/60) / ctr) * (vocabsize-ctr))[:5]+'  minutes)')
            sys.stdout.flush()
            ctr+=1
            if self.ver==1:
                self.domain_specific_importance[term] = (1 + math.log1p((self.legalidf[term] * self.legalcf[term]) / (self.nonlegalcf[term] * self.nonlegalidf[term] + 1)))
            elif self.ver==2:
                self.domain_specific_importance[term] = (1 + math.log1p(self.legalcf[term])*self.legalidf[term]) /   (1.0+math.log1p(self.nonlegalcf[term])*self.nonlegalidf[term])
        return

    def fit_legal(self, legal_tokenized_documents):
        self.start_time = timeit.default_timer()
        print ('\nstarted calculating legal frequencies...')
        (self.legalidf , self.legalcf ) = self.calculate_frequencies(legal_tokenized_documents, normalize=True)
        exclusive_nonlegal_tokens = list(set(self.nonlegalcf.keys()) - set(self.legalcf.keys()))
        exclusive_legal_tokens = list(set(self.legalcf.keys())- set(self.nonlegalcf.keys()))
        for tkn in exclusive_nonlegal_tokens:
            self.legalcf[tkn]=0
            self.legalidf[tkn]=0
        for tkn in exclusive_legal_tokens:
            self.nonlegalcf[tkn]=0
            self.nonlegalidf[tkn]=0
        print ('\nstarted calculating domain_specific_importances...')
        ctr=1
        cf_start_time = timeit.default_timer()
        vocabsize = len(self.legalidf.keys())
        for term in self.legalidf.keys():
            sys.stdout.write('\r')
            sys.stdout.write('DSI for '+str(ctr)+' token out of '+str(vocabsize)+'   '+str((ctr*100.0)/vocabsize)[:6]+'% done  (Time elapsed = '+str(float(timeit.default_timer() - start_time)/60)[:5]+'  minutes)   (ETA = '+str((float((timeit.default_timer() - cf_start_time)/60) / ctr) * (vocabsize-ctr))[:5]+'  minutes)')
            sys.stdout.flush()
            ctr+=1
            if self.ver==1:
                self.domain_specific_importance[term] = (1 + math.log1p((self.legalidf[term] * self.legalcf[term]) / (self.nonlegalcf[term] * self.nonlegalidf[term] + 1)))
            elif self.ver==2:
                self.domain_specific_importance[term] = (1 + math.log1p(self.legalcf[term])*self.legalidf[term]) /   (1.0+math.log1p(self.nonlegalcf[term])*self.nonlegalidf[term])
        return
