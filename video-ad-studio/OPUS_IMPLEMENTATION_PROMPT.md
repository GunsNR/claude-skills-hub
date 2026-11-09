# Video-ad studio: implementation prompt for Claude Opus 5.5

Facts in this prompt were checked on 2026-11-09. Prices and licences change, so
the prompt tells Opus to re-check them.

## How to use this (5 steps)

1. On your PC, make a new empty folder for this business, for example
   `C:\Users\izzy\Projects\video-ad-studio`. Keep it out of the Smart OS folder
   and out of any public repo.
2. Open Git Bash in that folder and run `claude`.
3. Type `/model` and pick **Opus 5.5**.
4. Press **Shift+Tab** until the bottom of the screen says **plan mode**.
5. Copy everything below the line that says `PROMPT STARTS HERE` and paste it in.
   If you have reference videos, paste the links under the prompt before sending.

Done looks like: Opus replies with a short plan and a list of approvals it needs,
and has not changed any files yet.

---

PROMPT STARTS HERE

You are building a small video-ad business for a solo owner, end to end: the
software that runs it, real rendered sample videos, the owner's own launch
advert, and a plain-English guide to operating it. I'll describe the owner, the
offer, the creative direction, and what "done" means. Where I give a reason,
use it to make good calls in situations I didn't cover.

## 1. Who this is for and how to work with them

The owner is an entrepreneur with limited coding knowledge, limited startup
money, and little patience for technical friction. They have ADHD and read best
when things are short, concrete, and ordered. They work on Windows with Git
Bash, so every command and path you give them has to work there.

This is a new business. The owner also runs an SEO agency; keep the two fully
separate and do not reuse that agency's branding, data, or client names.

Working rules:

- Start by confirming the target folder and reading any project instructions
  in it. If the folder holds existing work, preserve it and tell the owner what
  you found before changing anything.
- Before any edit, say in two or three lines what you will change and which
  files are affected. Make small commits. Never put a secret, key, or token in
  a file, a commit, or a message.
- Ask before anything that costs money, installs software, uploads to a third
  party, deploys, publishes, or sends a message to anyone. One approval covers
  one action.
- Resolve routine choices yourself and label them as assumptions. Ask at most
  three questions at a time, and only when the answer changes the result.
- Report honestly. Say what works, what is partly built, and what you did not
  test. Never invent customer evidence, testimonials, results, or numbers.

## 2. The business and the offer

The business sells professional short video adverts to five kinds of buyer:
product and ecommerce brands, SaaS companies, roofing contractors, HVAC
companies, and construction businesses.

Working name: **Onetake Video Ads**. This is a placeholder. Store it once in
config so it can change everywhere, and note that the owner still has to check
the domain and trademark.

The headline offer is "Professional video ads for your business from $150."

**Starter package ($150):** one 15 to 30 second advert, one concept, one aspect
ratio, burned-in captions, client-supplied or properly licensed assets, and one
revision round. Usage covers the client's website, social media, and online
ads. Recommend payment in full before production starts, and present that as
the owner's decision.

**Quoted separately:** custom 3D modelling, filming, large amounts of generated
footage, extra aspect ratios, extra revision rounds, rush delivery, and
broadcast use. Broadcast is separate for a real reason: the free music licence
checked for this project allows online ads but not TV or radio.

Propose add-on prices in a pricing config, and mark every one as a proposal for
the owner to confirm.

**Unit economics.** Build a cost worksheet the owner can edit. Keep estimated
and measured costs in separate columns, and replace estimates with measured
figures as real jobs complete. Starting estimates, all assumptions unless
marked:

| Line | Starting figure | Status |
| --- | --- | --- |
| Price | $150 | Set by owner |
| Card fee at 2.9% + $0.30 | $4.65 | Rate checked 2026-11-09; invoice-tool fees not checked |
| Claude plan share per order | $2.50 to $12.50 | Assumes a $20 or $100 monthly plan spread over 8 orders |
| Stock assets and music | $0 to $15 | Assumes free-licence sources for most jobs |
| Rendering and storage | $0 to $2 | Assumes local rendering; measure it |
| Owner labour | 2 to 3 hours once templates exist, 5 to 8 hours for early jobs | Unmeasured |
| Getting the customer | Unknown | Track time and any ad spend per paid order |

On those figures the cash left before labour is roughly $115 to $140 per order.
The offer only works if production stays template-based and close to three
hours, so design the whole system around protecting that time. Show the owner
the effective hourly rate at 3, 6, and 8 hours.

Keep the worksheet with real figures and all client data out of version
control.

## 3. The owner's own advert

The business's launch advert is the main creative deliverable and the main
demonstration on the website. It should make a buyer think "I want that for my
business."

**Brand idea: stop describing, start showing.** Everything begins as plain type
and comes alive. Use that one idea across the adverts and the website.

**Opening line.** Present all three to the owner, then build with the
recommended one:

- A, the owner's original: "The most scintillating way to describe your
  business..."
- B: "Your business, brought to life in 30 seconds."
- C, recommended: "Stop describing your business. Show it."

C is recommended because it reads in under two seconds with the sound off, a
roofer and a SaaS founder both understand it instantly, and it sets up the
closing line. Keep A as a test variant for product and ecommerce audiences.
Treat this as a hypothesis until real results exist.

**Promise.** Keep it concrete: a professionally produced video the client can
reuse across the agreed channels. Any claim about lasting or perpetual use has
to be backed by the licence of every asset in that video. Do not promise sales,
attention, or unlimited use.

**Flagship advert, about 40 seconds.** Start from this storyboard and improve
the timing where it helps:

| Time | Beat | What the viewer sees |
| --- | --- | --- |
| 0:00 to 0:02 | Hook | Flat words "YOUR BUSINESS" on a dark stage. Line: "Stop describing your business." |
| 0:02 to 0:05 | Turn | "Show it." The letters gain depth and reshape into a product. |
| 0:05 to 0:11 | Product | A lit 3D product reveal: convincing materials, a purposeful camera move, sharp detail. |
| 0:11 to 0:17 | SaaS | A 2D animation: a recognisable mess becomes one clear product benefit. |
| 0:17 to 0:27 | Home services | Roofing, HVAC, then construction: equipment, process, workmanship, useful service facts. |
| 0:27 to 0:34 | Offer | "Professional video ads from $150" with what the starter package includes. |
| 0:34 to 0:38 | Close | "One video. One payment. Your business, brought to life." |
| 0:38 to 0:42 | Action | "Tell us about your business." plus the web address. |

Every transition should carry an idea from one scene into the next, for example
a match cut on a shape or a line of type that becomes the next object. The
result has to feel like one directed advert, so reject any cut that only looks
impressive.

Deliver for the flagship: a timed script, voiceover script, on-screen text,
storyboard, shot list, transition notes, music and sound direction, asset list,
and production instructions. Develop the owner's closing idea, "One time. One
video. One payment. A lasting piece of advertising material for your business",
into natural sales copy that keeps the excitement and the one-time-purchase
appeal.

**Five audience versions, about 15 seconds each:** product and ecommerce, SaaS,
roofing, HVAC, construction. Each needs its own opening, its own visual proof,
the buyer's real worry, the benefit, and a call to action. Change the story and
the imagery for each buyer. Swapping only the business name is not enough.

Use the flagship for the website's main introduction and the five versions on
the matching portfolio pages and campaigns.

**Attribution.** Give each version its own tracked link. Store the version and
campaign on every inquiry, and add a "how did you hear about us" field. In the
studio, show per version: inquiries, qualified inquiries, paid orders, cost to
get a customer, and contribution margin. Those four are how success is judged.
Present any testing advice as a hypothesis.

## 4. Reference videos

The owner may paste one or two YouTube links or other references below this
prompt. If none are there, continue, and list which creative decisions stay
provisional until references arrive.

Analyse references with the Watch skill from `bradautomates/claude-video`, or
an installed equivalent. A transcript alone is not enough, because the point is
the visuals. Before using it:

- Check which video skills and dependencies are installed. An instruction file
  being present does not mean the tool is configured and working, so test it.
- Say what runs locally and what needs an outside service. Watch's fast path
  sends video to Google's Gemini API and needs a key the owner creates and
  saves themselves. Its local path needs ffmpeg and yt-dlp, plus Deno for
  YouTube.
- Get approval before any install, paid service, or upload. Use the exact repo
  name, because lookalike projects exist.
- Leave original footage and existing project files untouched.

For each reference, produce a timestamped breakdown: opening hook and story,
shot lengths and editing rhythm, camera movement, lighting, materials and
composition, typography and on-screen text, animation and transitions, music,
sound effects and voiceover, how the offer and call to action are shown, and
the principles worth adapting. Check the important timestamps against actual
frames, mark each finding verified or unverified, and say what you could not
see.

References inform original work. Do not copy footage, scripts, branding, or a
distinctive sequence.

## 5. Tools

Take stock of what is installed before recommending anything new, and choose
the smallest set that does the job. Findings from 2026-11-09, to be re-checked
if you are reading this more than a month later:

- **Remotion** is the main engine for compositions, captions, and 2D motion.
  Its licence is free for individuals and companies of up to three people,
  including commercial use. Larger companies pay. Remotion agent skills may
  already be installed; use them.
- **3D:** start with `@remotion/three`, which runs React Three Fiber inside
  Remotion so 3D renders in the same pipeline with no extra install. Three.js
  needs the `angle` OpenGL setting when rendering. Poly Haven lighting and
  texture assets are CC0. If the product reveal does not look convincing,
  propose Blender as an upgrade. Blender is GPL, free for commercial work, and
  what you render is yours, but it is a separate install that needs approval.
- **FFmpeg** handles trimming, assembly, audio levels, encoding, and exports.
- **Voiceover:** design every advert to work with the sound off, and always
  deliver the voiceover script and timings. A voice tool needs approval. On the
  ElevenLabs pricing page a commercial licence starts at the $6 a month plan
  and is not listed on the free plan. A local text-to-speech model is an
  option, but check its licence first. Default to a male voice.
- **Not recommended as the base:** HyperFrames (HTML to video, Apache-2.0) is
  popular and capable, but a second engine doubles what a beginner has to
  maintain. The `product-launch-video` skill from EveryInc is small and has
  not been updated since April 2026; borrow its habits (storyboard before
  code, check one still per scene, a separate composition per aspect ratio)
  without installing it.

When a capability is missing, search with `npx skills find` or the host's own
discovery. Before proposing an install, read the skill's files and report its
source, compatibility, dependencies, commercial terms, and cost. Install counts
alone prove little, since some listings with large counts are near-copies of
well-known skills.

You orchestrate production. Realistic footage comes from the client, from
properly licensed stock, or from a video-generation service the owner has
separately approved.

## 6. The system to build

**First slice, working end to end:** complete intake, save the project, approve
the brief, render a video, export the deliverable. Build this before anything
else, for one owner.

**Stack.** Use Next.js with TypeScript for the public site and the private
studio, SQLite for storage, Remotion compositions in the same repository, and a
separate render worker that takes jobs from a queue so rendering never runs
inside a web request. Pick a SQLite driver that installs on Windows without a
compiler, and verify it. If you see a clearly simpler route to the same result,
propose it before building.

**Requirements:** persistent storage, input validation, recoverable errors,
operator pages behind a login, credentials only on the server, readable render
logs, failure messages that say what to do next, commands that can be re-run,
and clear output locations.

**Data.** Keep it minimal: inquiries with attribution, clients, projects, brand
kits, briefs, script and storyboard versions, production assets, references,
render jobs, versions and deliverables, feedback, cost lines split into
estimated and actual, and a status history. Store shared campaign inputs such
as price, package terms, and contact details once, so an approved change
reaches every advert and page.

**Project states:** inquiry, brief drafted, brief approved, script approved,
assets cleared, rendering, internal review, client review, revision, approved,
delivered, closed, plus on hold and cancelled. Enforce these gates:

- No render until the brief and script are approved, every asset's rights are
  cleared, and the casting check has passed.
- One revision is included. A second needs a paid add-on recorded first.
- No delivery until the quality checklist is complete and the owner releases it.

**Production flow:** client brief, audience and offer, script, storyboard,
asset selection, approval, render, quality review, revision, delivery.
Automate project folders and briefs, applying brand colours, logos, fonts and
contact details, audience-specific draft scripts, reusable scene compositions,
rendering approved variations, captions and format exports, and tracking of
versions, costs, and delivery files.

Keep a human approval for factual business claims, script and storyboard
choice, asset rights, casting compliance, and final release.

**Money and messages.** Manual invoices and prepared client messages are fine
for now. The owner marks a payment as received. Never simulate a completed
payment and never send a message automatically.

**Public website.** Expressive, memorable, and led by the work. Show real
rendered video immediately. Include the flagship advert, playable audience
examples, portfolio filtering, clearly scoped packages, process, FAQs, a
persuasive intake flow, and an obvious "Start my video" action.

**Private studio.** Calm and efficient. Show project statuses and the next
action, client briefs and brand assets, scripts and storyboards, reference and
licence records, estimated and actual costs, feedback, versions, rendering,
and exports.

**Visual identity.** Define it through typography, composition, colour,
spacing, imagery, and purposeful motion. Starting direction: a near-black
stage, warm off-white type, and one strong signal accent, with a tint per
industry. Use one expressive display typeface and one highly readable text
face, both openly licensed and recorded in the asset register. Motion treats
type as a material that unfolds into objects. The studio uses the same identity
at low volume: light, quiet, and dense without feeling busy.

For the studio's components, evaluate Meta's Astryx design system
(`meta/astryx`, MIT, React 19 and StyleX, built for agents). Install it the way
its README says and do not guess package names. Give it a 30 minute trial. If
setup fights the stack, fall back to your own small component set and say so.
For the public site, use the owner's own hero and landing-page skills if they
are installed, then a front-end design skill.

Provide responsive layouts, keyboard access, reduced-motion behaviour, readable
contrast, and useful empty, loading, error, and success states.

Label every fictional demonstration as fictional. Use only real testimonials,
client claims, and results, which means none at launch.

Explain local setup, and separately list what a secure hosted launch would
need. Do not deploy.

## 7. Portfolio examples

Develop five complete concepts: product in 3D, SaaS in 2D, roofing, HVAC, and
construction. For each, supply the fictional business, audience, message, timed
script, storyboard, asset needs, production method, effort estimate, and call
to action.

Render at least three real, playable sample videos: product in 3D, SaaS in 2D,
and one home-service example. Finish the other home-service versions as
production-ready briefs in the same system.

For home-service scenes, the default is designed, code-drawn sequences, such as
a roof assembling layer by layer or airflow through a cutaway house, because
they need no licence and no approval. Add licensed stock footage only after the
owner approves each clip.

Reuse the original sample scenes inside the flagship advert. That keeps cost
down and makes the flagship a true showcase of the same work.

Check caption readability, safe areas, intentional crops, audio balance,
timing, and that each export plays. Never present generic footage as a
client's real projects, staff, or customers.

## 8. Casting preference

This is the owner's standing default for everything the business produces:

- Do not use live-action women.
- Prefer products, buildings, equipment, environments, and male presenters or
  workers.
- Animated women may appear only with modest, conservative, family-friendly
  clothing and presentation.

Apply it to intake defaults, briefs, asset selection, generation prompts,
reference adaptations, and final review. Check background footage and crowds
too. Record a casting check on every asset and make it a gate before rendering.
A client's brief can only change this default with the owner's approval.

## 9. Research and records

Review these as reference sources and explain what each teaches: Meta Ad
Library, TikTok Creative Center, Google Ads Transparency Center, Vimeo Staff
Picks, and relevant production studios. These are for study only.

For production assets, evaluate client-supplied material, Pexels, Mixkit, and
suitable alternatives, and check the licence of each individual asset. Notes
from 2026-11-09: the Pexels licence allows free commercial use without credit
but forbids implying that identifiable people or brands endorse a product.
Mixkit's free music licence allows online ads and social video but not TV,
radio, CDs, or games. Mixkit's stock video terms were not readable that day, so
open them yourself, including its restricted licence.

Keep two separate registers. The reference register is for material you study
and never ship. The production-asset register records each asset's origin,
licence, credit requirement, permitted distribution, and casting check.

Verify current tool prices and licences. Free software still has a cost in
time, hardware, and retries, so count it.

## 10. Playbook and campaign materials

Write a beginner-friendly playbook in plain English, with short steps and a
"done looks like" line for each. Cover:

1. Installing what is needed and running the system.
2. Creating and publishing the first portfolio after approval.
3. Finding suitable prospects.
4. Presenting the $150 offer.
5. Collecting usable briefs and assets.
6. Quoting and getting creative approval.
7. Producing and reviewing an advert.
8. Handling the included revision.
9. Collecting payment and delivering files.
10. Tracking profit and earning repeat orders.

Include a first-week checklist with tasks of 10 to 45 minutes, and one complete
worked example from inquiry to delivery.

Also provide: website copy, the flagship script, the five audience scripts,
outreach email and direct-message drafts, a discovery-call outline, a proposal,
a short revision policy, and a delivery message. These are drafts for the owner
to send. You send nothing.

## 11. Testing and acceptance

- Write working code and real project files.
- Test real behaviour: persistence, pricing sums, project state changes and
  their gates, validation, and rendering. For rendering, produce a short video
  and confirm its length, size, and audio track with a probe tool.
- Check desktop and mobile layouts in a real browser.
- Do one batched visual review of the site and the videos, fix everything from
  it together, and confirm once.
- Show the owner the visual work and get approval before committing it.

Deliver a README, a configuration example, seed demonstrations, render
instructions, the playbook, campaign materials, the cost worksheet, and a dated
source list with links.

## 12. Order of work and final report

1. Confirm the folder, take stock of tools and skills, and reply with a short
   plan plus every approval you need. Change nothing yet.
2. Build the first working slice and test it.
3. Build the sample scenes, then assemble the flagship from them.
4. Build the public site and the studio around the real videos.
5. Write the playbook, campaign materials, worksheet, and source list.
6. Run the review and tests, then report.

Your final report states, in this order: what works, how to run it, where the
outputs are, what you tested and the results, what is incomplete or only partly
integrated, and what needs the owner's account, money, or decision. Lead with
what works and keep it short enough to read in two minutes.
