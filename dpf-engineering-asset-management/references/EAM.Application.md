---
id: EAM.Application
title: "EAM.Application:1 - APP-EAM-01 - One asset and a supported value comparison"
---

# EAM.Application: EAM.Application:1 - APP-EAM-01 - One asset and a supported value comparison

---

## EAM.Application:1 - APP-EAM-01 - One asset and a supported value comparison



### EAM.Application:1.1 - Shared CityWater premises

CityWater 2027 is a fictional utility with twelve pumping stations in two service areas. A and C are in North; B and D are in East; the other eight stations supply the remaining capability and are unchanged by the compared options. A, B and D have abnormal vibration. Existing, case-supplied diagnostic accounts distinguish their conditions and support the particular interventions below; the vibration label alone supplies neither diagnosis nor a life estimate.

The case supplies an existing water-delivery mandate issued by CityWater's water-service authority. It requires water of the stated quality and minimum delivered North/East rates of 700/700 m³/h during the dry work window and 1,100/900 during the wet season. The case assigns revision of this mandate to the water-service authority; the infrastructure committee chooses the asset programme within it.

Separately, the supplied operating account gives normal usable North/East capability of 1,000/1,000 m³/h. The wet-season North requirement exceeds present usable capability by 100 m³/h. Both shortlisted C options add 200 m³/h, either by modification or by a qualified leased service. The 200 is the contribution of these options, not an unstated minimum increment. During a dry-window outage, A removes 200 from North and C removes 300; B and D each remove 200 from East. One A or C outage fits the dry requirement, but their simultaneous outage gives only 500 and does not. Simultaneous B and D outages leave 600 in East and also fail. These are finite supplied service bounds, not a hydraulic model or a probability of reliability.

The case additionally supplies applicable engineering and service-risk qualifications for each shortlisted policy, including the supported fallback and response to abnormal conditions. Their boundaries cover the stated duty and horizon. No claim about every contingency or a new real equipment limit is derived from the simple supply totals. If a qualification is absent or invalidated, [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) removes that option from the eligible comparison and returns the missing specialist question. Lower financial cost does not repair the missing qualification.

The comparison horizon is the five years beginning with the initial 2027 decisions. All values are constructed millions of constant-price euros, from the utility's stated perspective. The real discount rate is 3% solely for this example. Initial capital and initial operating cash occur at time zero; recurring costs occur at each year end; residual value occurs at the end of year 5. The supplied terminal values represent remaining service value, net of the stated exit costs, on the same basis for every option. A different sale/withdrawal decision needs its own terminal-value basis. Different technical lives do not disappear at the five-year boundary.

The annual amounts include the specified energy, routine maintenance, inspection, contingent response and continuing service costs under each policy; do not add them again as a separate generic risk allowance. A material unpriced consequence remains outside the sum and must retain its own criterion. Historical expenditure is sunk for this future choice. Accounting depreciation is not an additional cash outflow. Financing and tax effects are held equal in this constructed comparison; a real difference would require explicit treatment by its supplying practice.

Define `a = Σ(t=1..5) 1/(1.03)^t = 4.579707187` and `d = 1/(1.03)^5 = 0.862608784`. For each option, `present cost = initial capital + initial operating cash + annual cost × a − terminal value × d`.

| Asset/option | Initial capital | Initial operating cash | Annual cost | Terminal value | Whole team/outage days | Present cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A: refurbish (`F`) | 2.0 | 0 | 0.30 | 0.40 | 2 | 3.028869 |
| A: replace (`R`) | 3.5 | 0 | 0.18 | 1.30 | 3 | 3.202956 |
| B: refurbish (`F`) | 2.0 | 0 | 0.35 | 0.40 | 2 | 3.257854 |
| B: replace (`R`) | 3.5 | 0 | 0.18 | 1.30 | 3 | 3.202956 |
| C: modify (`M`) | 3.0 | 0 | 0.20 | 0.80 | 3 | 3.225854 |
| C: leased service (`L`) | 0 | 0 | 1.20 | 0 | 1 | 5.495649 |
| D: continued-use policy (`K`) | 0 | 0.50 | 1.00 | 0 | 1 | 5.079707 |
| D: replace (`R`) | 3.0 | 0 | 0.35 | 1.20 | 3 | 3.567767 |

Each duration includes the required isolation, intervention, testing and return for that option, using one already qualified and available team. Prerequisite design, procurement and non-outage preparation are supplied as complete before the window. Days denote the same staffed whole-work windows in both the calendar and the estimates; they are not individual person-days. These are teaching inputs, not equipment procedures or industry duration norms. For a real case, use the [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation) result rather than assuming those inclusions.

The D continued-use policy is a supported five-year service policy with the specified initial maintenance intervention, recurring maintenance, response and backup provisions. It is not an unsupported extrapolation of a one-year condition forecast. The case's qualification is conditional on unchanged duty and the identified failure mechanism; a new structural finding invalidates it. No new diagnosis, repair effectiveness or permission is inferred from the economic calculation.



### EAM.Application:1.2 - The request about D and its answer

The infrastructure committee asks the EAM practitioner whether D should continue under the supported maintenance policy or be replaced now, assuming both choices have funding and a suitable window. MNT can adequately recommend the 0.50 intervention for maintained functioning. EAM asks the additional value question at the same service and horizon.

Continued use costs `0.50 + 1.00 × a = 5.079707`. Replacement costs `3.00 + 0.35 × a − 1.20 × d = 3.567767`. Replacement saves 1.511940 in present cost within the admitted comparison. The completed result can therefore be a recommendation to replace, qualified by the supplied service, engineering, funding and timing conditions. It is not a work order or a hand-back result.

The comparison also gives a useful stop for inquiry. Holding the other inputs fixed, continued use and replacement are equal when the continued-use annual cost is 0.669861. An existing justified range of 0.95–1.05 does not reverse the recommendation, so a new cost investigation solely to decide between these options is unnecessary. A credible annual cost of 0.60 would reverse that economic choice; a credible result about that possibility could be useful if obtainable in time at a justified total burden. This is sensitivity, not a probability distribution. The EAM practitioner uses the specialist's engineering assessment of D's stated duty and the water-delivery mandate in the shared premises above to establish which policies remain eligible. The sensitivity calculation answers only the cost question.

If the operator asks only about present condition or the intervention needed to maintain the already selected use, the maintenance practitioner can answer by supplying the applicable condition account or intervention recommendation. The operator receives that bounded maintenance answer. When the question is instead which asset option offers better value over this horizon, the EAM practitioner supplies the additional comparison even though there is only one asset.



### EAM.Application:1.3 - When the complete policy is still missing

The D comparison above starts from complete, supported policies. When a new request instead supplies only an initial repair price, [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) constructs the policy before [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) compares it. In its separate asset E case, initial work supports three years but the service is required for four; the further overhaul, its window and temporary service belong to the alternative. Omitting that work reverses the apparent cost preference while leaving year four unsupported.

[FIN.6](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin6---value-capital-projects) supplies the dated financial account for the stated technical policy, and [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation) supplies its ending valuation. Moving only the end of the explicit table to year two requires a value that represents the same later cash and ending premise; [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) shows that the whole present cost and preference remain unchanged. Ending the service at year two instead changes the required policy and uses actual exit consequences. A different supplied valuation must be reconciled to its changed assumptions before it can change the recommendation. If an observation later changes technical support or the ending premise, [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) returns the affected policy to [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) and the comparison. D's supplied five-year premises and the programme calculation below remain their own case.



## EAM.Application:2 - APP-EAM-02 - The same asset in a constrained programme

CityWater's funding board has allocated 8 for initial capital, a separate 0.60 for initial operating expenditure and 3 for annual operation. The infrastructure committee is authorized to select the asset programme within those allocations; changing an allocation requires a decision by the funding board. The operating plan separately supplies twelve available team/outage days before the wet season. These allocations, authorities and operating conditions are constructed case premises. No later funding is assumed in this base comparison. Each station needs exactly one of its two qualified options. For this small problem, enumerate all sixteen combinations; do not rank individual condition scores or savings ratios.

Codes below follow asset order A/B/C/D. Every row satisfies the initial and recurring operating allowances and the twelve-day bound; the base funding column identifies the remaining capital constraint. The service checks still require a non-overlapping schedule for the connected outages.

| Combination | Initial capital | Days | Total present cost | Base funding eligible? |
| --- | ---: | ---: | ---: | --- |
| `FRMR` | 11.5 | 11 | 13.025446 | capital exceeds 8 |
| `FFMR` | 10.0 | 10 | 13.080344 | capital exceeds 8 |
| `RRMR` | 13.0 | 12 | 13.199533 | capital exceeds 8 |
| `RFMR` | 11.5 | 11 | 13.254431 | capital exceeds 8 |
| `FRMK` | 8.5 | 9 | 14.537386 | capital exceeds 8 |
| `FFMK` | 7.0 | 8 | 14.592284 | yes |
| `RRMK` | 10.0 | 10 | 14.711473 | capital exceeds 8 |
| `RFMK` | 8.5 | 9 | 14.766371 | capital exceeds 8 |
| `FRLR` | 8.5 | 9 | 15.295240 | capital exceeds 8 |
| `FFLR` | 7.0 | 8 | 15.350138 | yes |
| `RRLR` | 10.0 | 10 | 15.469327 | capital exceeds 8 |
| `RFLR` | 8.5 | 9 | 15.524225 | capital exceeds 8 |
| `FRLK` | 5.5 | 7 | 16.807180 | yes |
| `FFLK` | 4.0 | 6 | 16.862078 | yes |
| `RRLK` | 7.0 | 8 | 16.981268 | yes |
| `RFLK` | 5.5 | 7 | 17.036166 | yes |

`FFMK` is the minimum-cost eligible combination: refurbish A and B, modify C and retain D under its supported policy. It uses 7 of capital, 0.50 of initial operating cash, 1.85 annually and eight team/outage days. Its total present cost is 14.592284. A feasible twelve-day calendar under these premises can place A on days 1–2, B on 3–4, C on 5–7 and D on 8, with four uncommitted days. Each restored station is available before another dependent station is removed. The uncommitted allowance does not establish that all disturbances fit.

The individual D recommendation remains true under its assumptions, but replacing D while retaining both refurbishments and C modification needs 10 of capital and is infeasible at 8. `FFLR` frees C's capital through leased service and replaces D, but costs 15.350138 overall. Thus merely swapping in the individually preferred D option is not the portfolio answer. The unused 1 of capital is not an extra benefit or an instruction to spend it.

Three separate changed-condition branches show the decision's sensitivity:

- With the funding board's capital allocation raised to 10 and the other premises unchanged, `FFMR` becomes best: both refurbishments, C modification and D replacement, present cost 13.080344 and ten days. The authorized funding change precedes reliance on that feasible set; a desired budget increase is not available money.
- With only seven team/outage days and the original capital limit, `FRLK` becomes best among the supplied options: refurbish A, replace B, lease C's added service and continue D. It takes seven days, 5.5 capital and costs 16.807180. A cheaper eight-day combination does not fit merely because each job fits separately. Another qualified team or extended window would be another explicit alternative with its own full cost and service implications.
- If a new engineering finding invalidates D's continued-use policy, remove every `...K` combination. At the original limits, `FFLR` is then best, at 15.350138 and eight days. The supported response changes before any attempt to justify D continuation by its affordability. If the leased service were also unavailable, return the resulting unmet service/funding condition to the responsible decisions.

The EAM team submits its programme recommendation to the infrastructure committee. The finance practitioner supplies cost estimates and an affordability assessment against the funding board's allocations; those allocations set the spending limits. The infrastructure committee selects and authorizes an asset programme that fits those limits and the water-delivery mandate. MNT and operating authorities subsequently determine the permissions and conditions for protected work and resumption. The team can deliver its supported recommendation before the committee decides; the team reports an authorized programme only after that decision is supplied.



### EAM.Application:2.1 - When the demand basis changes

The original sixteen combinations use the supplied North wet-season requirement of 1,100 m³/h. Suppose a later, separately qualified demand account gives 1,250 for a period the asset choice must cover. [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) establishes its component basis, coincidence and status as a forecast or commitment; its Westbank example shows that construction with separate teaching inputs. [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) then compares the new scenario with the 1,200 contribution supported by either current C option. The 50 m³/h gap means none of the sixteen existing combinations supplies that scenario. Re-ranking their costs cannot repair the missing service.

Return to [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) for an additional supported contribution or a qualified demand-management alternative, then compare the resulting policies and combinations on the revised premises. A proposal to change the service obligation goes to its actual authority. The original programme calculation remains applicable to its original conditions. If later observations reveal the changed driver, [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) reopens this affected account and its option consequences.



### EAM.Application:2.2 - When a shared dependency changes recovery

A common dependency can require another option even when the normal-demand comparison passes. [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence)'s separate feeder example shows both units losing their contribution together, reserve exhaustion before full recovery, and an independent supply whose time to usable service changes the result. Its qualified recovery conditions become inputs when developing alternatives with [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) and EAM.8 and a calendar with [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies). A favourable price or available team does not restore the missing service.

To apply that construction to CityWater, obtain the relevant dependency, deliverability, usable reserve and restoration account for its actual service boundaries. Compare the resulting options in [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) and EAM.10 and retain the relied-on recovery conditions in the recommendation. The original CityWater outage bounds remain useful for the situations they describe. If an observed restoration time or dependency changes, [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) returns to the affected capability, option and timing.



### EAM.Application:2.3 - When shared work changes the consequences

The sixteen rows above use their declared additive costs and whole-work times. They do not establish whether a different work arrangement could share a mobilization, require extra temporary service or change a later commitment. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations)'s separate P+Q/Z case shows why that question matters: one qualified shared mobilization makes the joint solution cost 3.8 against the alternative's 3.9, while two required visits make it cost 4.0.

For a proposed CityWater arrangement, [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) must establish its actual windows and whole work, and [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) its service conditions. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) then reconstructs that combination's consequences; [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) supplies the financial return if joint cash or dated funding must be developed. Recompute the affected rows rather than applying a discount to all sixteen. If the change also affects demand, recovery or a continuing policy, return that premise to [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions), [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) or EAM.8. The existing capital, time and D-qualification branches remain valid on their stated premises.



### EAM.Application:2.4 - What subsequent outcomes and practice questions would mean

The programme promises the qualified added service from C, continued supported use of D and the stated spending. Completion of the work alone establishes none of those whole-programme outcomes. [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) shows how an obtained variance changes a particular premise, without inferring a technical cause from cost alone.

The later practice examples are separately constructed continuations. [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) compares a small responsibility/information repair with a new application. [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) compares a condition-priority rule with complete combination comparison and distinguishes a desk result from a trial in real decisions. [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) examines teaching, later use and selection of the reusable practice with different evidence. An observed asset selection is not automatically selection of the Method that helped produce it.

## EAM.Application:End
