#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
GOLDENS = ROOT / "goldens"


def fact(category, canonical, rationale, evidence, questions, required, invalid):
    return {
        "category": category,
        "canonical_fact": canonical,
        "rationale": rationale,
        "evidence_ids": evidence,
        "questions": questions,
        "required_concepts": required,
        "invalid_claims": invalid,
    }


MEMORIES = {
    "ATLAS": [
        fact("scope", "Atlas phase 1 covers enterprise onboarding only; SMB onboarding is deferred.", "The two segments have materially different operating models, and narrowing scope protects the launch window without permanently cancelling SMB work.", ["TM-00001", "OL-00001", "TR-00001", "SP-00005"], ["What is in Atlas phase 1?", "Was SMB onboarding included in the first Atlas release?"], ["enterprise onboarding", "SMB deferred", "phase 1"], ["SMB is included in phase 1", "Atlas supports all customer segments in the pilot"]),
        fact("data_authority", "CRM remains authoritative for customer identity and onboarding status; Atlas owns orchestration rather than a competing customer master.", "This avoids duplicate identity ownership, reconciliation ambiguity and divergent client-facing status.", ["TM-00013", "OL-00008", "CF-00001", "SP-00001"], ["Which system owns customer identity for Atlas?", "Does Atlas create its own customer master?"], ["CRM authoritative", "customer identity", "Atlas orchestration"], ["Atlas is the customer system of record", "Atlas may create a local master when CRM lookup fails"]),
        fact("dependency", "The Atlas pilot authenticates through Harbor's interim SSO bridge rather than waiting for Harbor's full migration.", "The bridge decouples the pilot schedule while keeping Atlas inside Harbor's identity-control boundary.", ["TM-00003", "CF-00002", "SP-00001", "OD-00001"], ["How does the Atlas pilot authenticate?", "Must Atlas wait for the complete Harbor migration?"], ["Harbor", "interim SSO bridge", "pilot"], ["Atlas uses local credentials", "Atlas waits for Harbor's full migration"]),
        fact("exception_control", "High-risk Atlas onboarding exceptions require accountable human approval.", "Legal, security and contractual exceptions need durable judgment, rationale and audit evidence rather than fully automated resolution.", ["TM-00049", "OL-00029", "CF-00003", "SP-00003"], ["Can Atlas automatically approve high-risk exceptions?", "What control applies to legal or contractual onboarding exceptions?"], ["high-risk exceptions", "human approval", "audit evidence"], ["all exceptions are automatically approved", "free-text notes count as approval"]),
        fact("process_governance", "Atlas uses a mandatory enterprise stage taxonomy while allowing governed region-specific substeps.", "The design preserves comparable enterprise reporting without erasing legitimate regional process detail.", ["TM-00025", "OL-00015", "CF-00004", "OD-00004"], ["Can regions define their own Atlas stages?", "How does Atlas balance global reporting with regional process?"], ["common stage taxonomy", "regional substeps", "governed"], ["each region may redefine enterprise stages", "regional variation is entirely prohibited"]),
        fact("cross_project", "Atlas depends on Harbor for authentication and shares CRM identity-quality concerns with Nova; these are distinct dependencies with separate owners.", "Authentication readiness and customer-data quality can each affect Atlas, but one dependency's status does not resolve the other.", ["TM-00003", "TR-00002", "SP-00001", "CF-00002"], ["What are Atlas's main cross-project dependencies?", "Does resolving Harbor authentication also resolve Atlas CRM quality?"], ["Harbor authentication", "Nova CRM identity quality", "separate dependencies"], ["Atlas has no cross-project dependencies", "Harbor owns CRM data quality"]),
    ],
    "PULSE": [
        fact("scope", "Pulse phase 1 alerts target store operations and explicitly exclude employee-level scoring.", "The telemetry and governance model were designed for operational conditions, not individual workforce judgments.", ["TM-00177", "OL-00076", "TR-00051", "CF-00045"], ["Does Pulse score individual employees?", "What does Pulse phase 1 alert on?"], ["store operations", "not employee-level scoring", "phase 1"], ["Pulse ranks employees", "employee performance scoring is a phase-1 feature"]),
        fact("latency", "Pulse accepts fifteen-minute analytical latency in phase 1 and defers real-time streaming.", "Predictable and explainable alerts on inconsistent telemetry were prioritized over sub-second processing.", ["TM-00213", "OL-00097", "TR-00052", "CF-00046"], ["Is Pulse real time?", "What analytical latency was accepted for Pulse?"], ["15-minute latency", "real-time deferred", "analytical"], ["Pulse requires real-time streaming", "Pulse guarantees sub-second alerts"]),
        fact("metric_governance", "Enterprise KPI definitions override legacy regional scorecard definitions in Pulse.", "A shared semantic layer is necessary for comparable reporting; regions may add context but cannot silently change enterprise calculations.", ["TM-00201", "OL-00090", "TR-00055", "CF-00049"], ["Which KPI definition wins when Pulse and a regional scorecard disagree?", "May a region redefine a Pulse enterprise KPI?"], ["enterprise KPI definitions", "override regional scorecards", "comparable reporting"], ["regional scorecards are authoritative", "each region may change KPI denominators"]),
        fact("rollout", "The Midwest region is Pulse's first production pilot.", "Midwest provides a controlled proving ground; pilot success still requires evidence before broader rollout.", ["TM-00189", "OL-00083", "TR-00053", "CF-00047"], ["Where is the first Pulse production pilot?", "Did Pulse launch to every region at once?"], ["Midwest", "first production pilot", "controlled rollout"], ["Pulse began with a global rollout", "Northeast is the first pilot"]),
        fact("dependency", "Pulse depends on shared analytical-platform capacity and batch windows coordinated with Orbit.", "Competing peak workloads require explicit scheduling and degradation rules rather than assuming unlimited capacity.", ["TM-00179", "TR-00054", "SP-00043", "OD-00034"], ["Which project shares platform capacity with Pulse?", "Why must Pulse coordinate batch windows?"], ["Orbit", "shared analytical platform", "batch capacity"], ["Pulse has dedicated unlimited compute", "Atlas owns Pulse batch capacity"]),
        fact("risk", "Missing telemetry and high false-positive rates are material Pulse operational risks.", "Either condition can make alerts misleading or unusable, so freshness, source quality and alert precision require explicit acceptance evidence.", ["TM-00178", "OL-00077", "TR-00051", "OD-00036"], ["What data-quality risks can undermine Pulse alerts?", "Why is alert precision part of Pulse readiness?"], ["missing telemetry", "false positives", "operational risk"], ["alert accuracy is not a release concern", "stale telemetry may be shown as current without warning"]),
    ],
    "NOVA": [
        fact("automation_boundary", "Nova recommends actions but cannot automatically change CRM opportunity stages.", "Commercial stage changes remain accountable human decisions; the integration must enforce the boundary rather than rely only on UI convention.", ["TM-00328", "OL-00140", "TR-00094", "CF-00085"], ["Can Nova update CRM opportunity stages automatically?", "What authority does a Nova recommendation have?"], ["recommendations", "cannot change CRM stages", "human accountability"], ["Nova autonomously advances opportunities", "a recommendation is authoritative CRM state"]),
        fact("evidence", "Every Nova recommendation must cite CRM, meeting or account-plan evidence.", "A recommendation without traceable evidence cannot be explained, reviewed or safely acted upon.", ["TM-00364", "OL-00161", "TR-00095", "CF-00086"], ["What evidence must a Nova recommendation provide?", "Can Nova issue an uncited recommendation?"], ["every recommendation", "cited evidence", "CRM meeting or account plan"], ["recommendations need no provenance", "model confidence substitutes for evidence"]),
        fact("pilot_access", "The Nova pilot is limited to strategic account directors.", "The restricted cohort supports controlled learning before access is considered for broader sales roles.", ["TM-00340", "OL-00147", "TR-00096", "CF-00087"], ["Who can use Nova during the pilot?", "Is the Nova pilot open to all sales staff?"], ["strategic account directors", "pilot", "limited cohort"], ["all sales employees have pilot access", "external customers are the pilot cohort"]),
        fact("authorization", "Nova may surface only evidence already visible to the requesting account team.", "Generated explanations, cached recommendations and snippets must not become channels for bypassing source permissions.", ["TM-00352", "OL-00154", "TR-00098", "CF-00084"], ["Can Nova reveal evidence the requester cannot access directly?", "How are evidence permissions applied in Nova?"], ["requesting account team", "existing permissions", "no leakage"], ["Nova access overrides source permissions", "a summary may reveal restricted evidence"]),
        fact("identity_dependency", "Nova depends on Atlas-related CRM customer and account identity quality.", "Ambiguous or duplicate account identities can attach evidence and recommendations to the wrong commercial entity.", ["TM-00330", "TR-00094", "OD-00062", "SP-00080"], ["What Atlas-related dependency affects Nova?", "Why does CRM identity quality matter to Nova?"], ["Atlas", "CRM account identity", "data quality"], ["Nova is independent of CRM identity", "Harbor owns customer matching"]),
        fact("authorization_dependency", "Nova depends on Harbor's account-team authorization mappings, separately from its Atlas identity dependency.", "A correct account match does not prove that the requester is authorized to see the account's evidence.", ["TR-00095", "CF-00084", "OD-00064", "SP-00079"], ["What Harbor capability does Nova rely on?", "Does correct account matching prove Nova evidence access?"], ["Harbor", "account-team authorization", "separate from identity"], ["identity matching automatically grants access", "Nova does not depend on Harbor"]),
    ],
    "HARBOR": [
        fact("migration", "Harbor migrates applications in waves based on criticality and provisioning readiness.", "A single date-driven cutover would ignore large differences in legacy integration, support ownership and recovery options.", ["TM-00496", "OL-00212", "TR-00142", "CF-00125"], ["How are Harbor migration waves sequenced?", "Does Harbor use one cutover date for every application?"], ["migration waves", "criticality", "provisioning readiness"], ["all applications migrate together", "schedule alone determines readiness"]),
        fact("access_model", "Role-based access control is Harbor's baseline, with documented and governed exceptions.", "Exceptions require ownership, rationale, compensating controls and review rather than becoming unofficial permanent roles.", ["TM-00532", "OL-00233", "TR-00143", "CF-00126"], ["What is Harbor's baseline access model?", "Are RBAC exceptions allowed without governance?"], ["RBAC baseline", "governed exceptions", "review"], ["all exceptions are prohibited", "local teams may create permanent unofficial roles"]),
        fact("atlas_bridge", "Harbor provides an interim SSO bridge for the Atlas pilot.", "The bridge lets Atlas proceed while preserving Harbor authentication controls and a retirement path.", ["TM-00508", "OL-00219", "TR-00144", "CF-00127"], ["What does Harbor provide to the Atlas pilot?", "Does Atlas use credentials outside Harbor?"], ["interim SSO bridge", "Atlas pilot", "Harbor controls"], ["Harbor has no Atlas dependency", "Atlas uses unmanaged local credentials"]),
        fact("legacy_apps", "Legacy applications without SCIM are not forced into Harbor phase 1.", "Forcing unsupported provisioning would hide manual revocation risk and operational cost; these applications need later waves or controlled interim procedures.", ["TM-00544", "OL-00240", "TR-00145", "CF-00123"], ["Are non-SCIM applications mandatory in Harbor phase 1?", "How does Harbor treat legacy provisioning gaps?"], ["legacy apps", "without SCIM", "not forced into phase 1"], ["every legacy app must migrate in phase 1", "manual provisioning is equivalent to SCIM"]),
        fact("privileged_access", "Privileged accounts require step-up controls before Harbor migration.", "Administrative identities have a materially higher blast radius and need stronger assurance than a successful standard login.", ["TM-00520", "OL-00226", "TR-00146", "CF-00124"], ["What must happen before privileged accounts migrate?", "Are standard login controls sufficient for Harbor administrators?"], ["privileged accounts", "step-up controls", "before migration"], ["privileged access can migrate without stronger controls", "standard authentication is always sufficient"]),
        fact("cross_project", "Harbor supports Atlas pilot authentication and Nova account-team authorization mappings as separate cross-project responsibilities.", "The two dependencies serve different consumers and must retain separate owners, timelines and acceptance evidence.", ["TM-00498", "TR-00143", "SP-00119", "CF-00123"], ["Which projects depend on Harbor?", "Are Harbor's Atlas and Nova dependencies the same capability?"], ["Atlas authentication", "Nova authorization mappings", "separate responsibilities"], ["Harbor supports only Atlas", "Atlas and Nova use the same dependency contract"]),
    ],
    "ORBIT": [
        fact("forecast_cadence", "Orbit uses a monthly rolling forecast instead of quarterly-only planning.", "The operating model updates assumptions more frequently while retaining version and rationale history.", ["TM-00697", "OL-00298", "TR-00199", "CF-00175"], ["What forecast cadence does Orbit use?", "Is Orbit limited to quarterly planning?"], ["monthly rolling forecast", "replaces quarterly-only", "version history"], ["Orbit forecasts only quarterly", "monthly updates erase prior versions"]),
        fact("financial_authority", "ERP actuals remain authoritative in Orbit; manual spreadsheet adjustments are governed exceptions.", "Orbit may transform and explain actuals but cannot establish a competing financial truth.", ["TM-00733", "OL-00319", "TR-00200", "CF-00176"], ["What is authoritative for Orbit actuals?", "Can a spreadsheet override ERP actuals by default?"], ["ERP actuals", "authoritative", "manual adjustments are exceptions"], ["Orbit is the source of record for actuals", "spreadsheet adjustments automatically replace ERP"]),
        fact("ai_boundary", "AI may draft Orbit variance narratives but cannot change forecasts.", "Narrative generation is an assistive use case; finance judgment remains responsible for forecast values and approved explanations.", ["TM-00745", "OL-00326", "TR-00202", "CF-00173"], ["Can Orbit AI change forecast values?", "What may AI do in Orbit?"], ["draft variance narratives", "cannot change forecasts", "human review"], ["AI autonomously updates forecasts", "AI narratives are automatically approved"]),
        fact("scenario_rollout", "Orbit scenario planning is phase 1 for finance leadership and phase 2 for broader business units.", "A controlled cohort validates scenario semantics and governance before wider rollout.", ["TM-00721", "OL-00312", "TR-00203", "CF-00174"], ["Who receives Orbit scenario planning in phase 1?", "Are all business units included immediately?"], ["finance leadership", "phase 1", "business units phase 2"], ["all business units are in phase 1", "scenario planning has no staged rollout"]),
        fact("dependency", "Orbit shares analytical-platform compute and batch windows with Pulse.", "Peak planning and store-processing workloads can contend, so capacity and service priorities require explicit coordination.", ["TM-00699", "OL-00305", "TR-00201", "SP-00167"], ["Which project shares platform capacity with Orbit?", "Why does Orbit coordinate batch windows?"], ["Pulse", "shared platform", "compute and batch windows"], ["Orbit has isolated unlimited compute", "Harbor schedules Orbit forecasts"]),
        fact("risk", "Platform-capacity contention and manual-adjustment governance are material Orbit risks.", "Capacity can delay forecast processing, while weak adjustment controls can obscure who changed a forecast and why.", ["TM-00698", "OL-00299", "TR-00203", "OD-00134"], ["What operational and governance risks matter to Orbit?", "Why must manual forecast adjustments be traceable?"], ["platform capacity contention", "manual adjustment governance", "traceability"], ["manual adjustments need no owner", "capacity cannot affect Orbit"]),
    ],
    "ORGANIZATION": [
        fact("hr_policy", "Meridian classifies roles as site-dependent, hybrid or remote-eligible; there is no universal office-day quota.", "Work-location expectations follow role needs, reasonable notice and documented temporary arrangements.", ["OP-00001", "OP-00002", "OP-00003"], ["Does Meridian mandate the same office schedule for every employee?", "How are Meridian work arrangements classified?"], ["role-based classification", "no universal quota", "HR review"], ["every employee has the same office-day requirement", "badge data is an individual productivity score"]),
        fact("hr_policy", "Meridian managers receive only the work restrictions needed to implement an accommodation, not an employee's diagnosis.", "Accommodation handling is confidential and separated from ordinary line management.", ["OP-00004", "OP-00005", "OP-00006"], ["Must an employee disclose a diagnosis to their manager?", "Can a project cancel protected leave for a release?"], ["confidential accommodation", "work restrictions", "HR process"], ["managers are entitled to diagnoses", "a milestone automatically cancels approved leave"]),
        fact("hr_policy", "Meridian performance decisions require documented evidence; telemetry or AI summaries cannot be the sole basis for a rating.", "Accountable manager judgment must consider agreed outcomes, quality, behavior and relevant constraints.", ["OP-00007", "OP-00008", "OP-00009"], ["Can activity telemetry determine a Meridian performance rating?", "May employees apply internally without manager permission?"], ["documented evidence", "not telemetry alone", "internal mobility"], ["AI assigns final performance ratings", "manager permission is required to apply internally"]),
        fact("it_policy", "Restricted Meridian data is accessed only from managed devices unless an approved exception provides equivalent controls.", "Remote access also requires MFA, and schedule pressure never authorizes personal email or unmanaged storage.", ["OP-00010", "OP-00011", "OP-00012"], ["Can an employee email work files to a personal account?", "What controls apply to remote Restricted-data access?"], ["managed device", "MFA", "no personal storage"], ["deadlines authorize personal email", "unmanaged devices may always access Restricted data"]),
        fact("it_policy", "Every Meridian account has an accountable owner; privileged work uses a separate elevated identity with step-up authentication.", "Shared privileged credentials are prohibited except for an attributed, time-bound emergency mechanism.", ["OP-00013", "OP-00014", "OP-00015"], ["Can Meridian administrators share a convenience account?", "How is privileged work authenticated?"], ["accountable owner", "separate elevated identity", "step-up authentication"], ["shared admin accounts are allowed for convenience", "standard identities should perform privileged work"]),
        fact("it_policy", "Meridian classifies data as Public, Internal, Confidential or Restricted, and approved human review is required before business use of generative-AI output.", "Removing names does not automatically authorize sensitive data for any AI service.", ["OP-00016", "OP-00017", "OP-00018"], ["What are Meridian's data classifications?", "Is de-identification enough to use any AI tool?"], ["four classifications", "approved AI use case", "human review"], ["all de-identified data may enter any AI tool", "AI output needs no review"]),
        fact("admin_policy", "A Meridian purchase request and required risk reviews must precede supplier commitment and production data access.", "Free trials do not bypass procurement when they involve data, integrations, renewal or contractual commitments.", ["OP-00019", "OP-00020", "OP-00021"], ["Can a team upload Meridian data to an unreviewed free trial?", "When must procurement review occur?"], ["purchase request before commitment", "vendor risk review", "no production data before approval"], ["free software never requires review", "requesters may approve their own purchases"]),
        fact("admin_policy", "Meridian travel and expenses require business purpose, timely evidence and independent approval; the lowest nominal fare is not always mandatory.", "Safety, accessibility, total journey time and changeability may justify a different reasonable option.", ["OP-00022", "OP-00023", "OP-00024"], ["Must Meridian travelers always choose the cheapest fare?", "Can an employee approve their own expense?"], ["reasonable cost", "business purpose", "independent approval"], ["employees approve their own claims", "lowest price always overrides safety"]),
        fact("admin_policy", "Meridian badges are individual and visitors use registered, attributable access; badges must not be lent even to colleagues.", "Reception or Security verifies identity and issues temporary access, while critical functions maintain tested continuity procedures.", ["OP-00025", "OP-00026", "OP-00027"], ["May an employee lend a badge to a colleague?", "What must Meridian critical functions maintain for disruption?"], ["individual badges", "registered visitors", "continuity procedures"], ["badge lending is acceptable between employees", "a site closure permits personal-storage workarounds"]),
    ],
}


def load_records(scope: str) -> dict[str, dict]:
    path = DATA / "organization" / "records.jsonl" if scope == "ORGANIZATION" else DATA / scope.lower() / "records.jsonl"
    return {record["id"]: record for record in (json.loads(line) for line in path.read_text().splitlines() if line.strip())}


def main() -> None:
    GOLDENS.mkdir(exist_ok=True)
    aggregate = []
    question_rows = []
    for scope, definitions in MEMORIES.items():
        records = load_records(scope)
        memories = []
        for number, definition in enumerate(definitions, 1):
            evidence = []
            for record_id in definition["evidence_ids"]:
                record = records[record_id]
                evidence.append({"record_id": record_id, "source": record["source"], "type": record["type"], "timestamp": record["timestamp"]})
            if len({item["source"] for item in evidence}) < 2:
                raise ValueError(f"{scope} golden memory {number} lacks source diversity")
            memory = {
                "id": f"{scope}-GM-{number:03d}",
                "scope": scope,
                "category": definition["category"],
                "status": "current",
                "canonical_fact": definition["canonical_fact"],
                "rationale": definition["rationale"],
                "valid_from": min(item["timestamp"] for item in evidence),
                "valid_to": None,
                "evidence": evidence,
                "evaluation": {
                    "questions": definition["questions"],
                    "required_concepts": definition["required_concepts"],
                    "invalid_claims": definition["invalid_claims"],
                },
            }
            memories.append(memory)
            aggregate.append(memory)
            for question_number, question in enumerate(definition["questions"], 1):
                question_rows.append({
                    "id": f"{scope}-GQ-{number:03d}-{question_number:02d}",
                    "memory_id": memory["id"],
                    "scope": scope,
                    "question": question,
                    "canonical_answer": memory["canonical_fact"],
                    "required_concepts": memory["evaluation"]["required_concepts"],
                    "invalid_claims": memory["evaluation"]["invalid_claims"],
                    "evidence_ids": [item["record_id"] for item in memory["evidence"]],
                })
        directory = GOLDENS / scope.lower()
        directory.mkdir(exist_ok=True)
        (directory / "golden_memories.json").write_text(json.dumps(memories, indent=2, ensure_ascii=False) + "\n")

    with (GOLDENS / "golden_memories.jsonl").open("w", encoding="utf-8") as output:
        for memory in aggregate:
            output.write(json.dumps(memory, ensure_ascii=False, separators=(",", ":")) + "\n")
    with (GOLDENS / "golden_questions.jsonl").open("w", encoding="utf-8") as output:
        for question in question_rows:
            output.write(json.dumps(question, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"golden memories: {len(aggregate)} facts and {len(question_rows)} questions across {len(MEMORIES)} scopes")


if __name__ == "__main__":
    main()
