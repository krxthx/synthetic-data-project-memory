# IT-002: Identity, Access and Privileged Administration

Policy owner: Elena Garcia, Chief Information Security Officer  
Approver: Priya Nair, Chief Information Officer  
Version: 1.5  
Status: Current  
Effective: 2026-02-15  
Review: 2027-02-15  
Supersedes: SEC-IAM-02 v1.4, effective 2025-08-15

## Identity principles

Every account must map to an accountable employee, contractor, approved external user or registered service owner. Access follows least privilege, separation of duties and job need. Possession of an account does not establish continuing entitlement: access can change when duties, location, contract, risk or system classification changes.

The authoritative worker lifecycle comes from approved HR and contingent-workforce records. Managers request role access; application owners approve access to their systems; Information Security defines control requirements. A requester's seniority does not replace approval evidence.

## Joiners, movers and leavers

Joiner access is based on an approved role and start date. Credentials are delivered through verified channels and are not activated early for convenience. Movers are assessed for both new access and access that must be removed. A manager must not preserve incompatible access merely because a handover remains incomplete.

Leaver access is disabled according to departure risk and timing. Involuntary or elevated-risk departures use coordinated HR, Legal, manager and security handling. Business information is transferred through approved ownership processes; another person must not sign in as the departing user. Tokens, sessions, keys, physical badges and third-party accounts are included in offboarding.

## Privileged and service access

Privileged work uses a separate elevated identity with step-up authentication, logging and restricted workstation or session controls where required. Administrators use standard accounts for email, browsing and routine collaboration. Permanent standing privilege is reduced where time-bound elevation can meet the operational need.

Shared privileged credentials are prohibited except for an approved emergency-access mechanism. Emergency access preserves individual attribution, limits duration, alerts control owners and triggers post-use review. It must not become the normal answer to a slow access request.

Service accounts have a named business owner and technical custodian, documented purpose, scoped permissions, credential-rotation method and review date. Credentials are stored in an approved secrets service and are not embedded in documents, scripts or tickets. Non-human identities are disabled when the service or integration is retired.

## Review, exceptions and evidence

Managers and application owners recertify access on the schedule set by system risk. Reviewers confirm current need rather than approving an entire list by default. Unanswered reviews escalate and may result in access suspension. High-risk conflicts are removed or covered by an approved compensating control.

Exceptions identify the access, reason, owner, expiry, risk and monitoring. Information Security approves them after application-owner justification. Evidence includes request, approvals, provisioning result, authentication events, privilege use, recertification and removal. Silence, an old ticket or prior access to another environment is not approval.
