import zipfile
import os

xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE simplemind-mindmaps>
<simplemind-mindmaps doc-version="3" generator="SimpleMindOSXN" gen-version="2.8.2">
    <mindmap>
        <meta>
            <guid guid="AA11BB22CC33DD44EE55FF66"></guid>
            <title text="Requirement Workflow"></title>
            <style key="system.blue-steel"></style>
            <auto-numbering style="disabled"></auto-numbering>
            <main-centraltheme id="0"></main-centraltheme>
        </meta>
        <topics>
            <topic id="0" parent="-1" x="0" y="100" text="Requirement Workflow" textfmt="plain" palette="1">
                <layout mode="free" direction="auto" flow="auto"></layout>
            </topic>

            <!-- CATEGORY: Not Started -->
            <topic id="10" parent="0" x="300" y="-150" text="Not Started" textfmt="plain" palette="2">
                <layout mode="list" direction="auto" flow="auto"></layout>
            </topic>
            <topic id="1" parent="10" x="550" y="-200" icon="ic8_48_note" text="New" textfmt="plain">
                <note>Category: Not started&#10;Requirement created / captured, not yet reviewed&#10;&#10;Responsible: Central Team / Vendor Team / Tenant Team</note>
            </topic>
            <topic id="2" parent="10" x="550" y="-100" icon="ic8_48_todo" text="To Do" textfmt="plain">
                <note>Category: Not started&#10;Requirement accepted, prioritized in backlog&#10;&#10;Responsible: Central Team / Vendor Team</note>
            </topic>

            <!-- CATEGORY: Active -->
            <topic id="11" parent="0" x="300" y="50" text="Active" textfmt="plain" palette="3">
                <layout mode="list" direction="auto" flow="auto"></layout>
            </topic>
            <topic id="3" parent="11" x="550" y="0" icon="ic8_48_measure" text="Analysis" textfmt="plain">
                <note>Category: Active&#10;Requirement scoped; Stories/Tasks being created; dependencies identified&#10;&#10;Responsible: Central Team / Vendor Team</note>
            </topic>
            <topic id="4" parent="11" x="550" y="100" icon="ic8_48_running" text="In Progress" textfmt="plain">
                <note>Category: Active&#10;Implementation underway - linked Stories/Tasks in Development; deployed to DEV for validation&#10;&#10;Responsible: Central Team / Vendor Team</note>
            </topic>

            <!-- CATEGORY: Waiting -->
            <topic id="12" parent="0" x="300" y="250" text="Waiting" textfmt="plain" palette="4">
                <layout mode="list" direction="auto" flow="auto"></layout>
            </topic>
            <topic id="5" parent="12" x="550" y="200" icon="ic8_48_question" text="Clarification" textfmt="plain">
                <note>Category: Waiting&#10;More information needed from stakeholders or tenant teams; questions documented in comments&#10;&#10;Responsible: Central Team / Tenant Team</note>
            </topic>
            <topic id="6" parent="12" x="550" y="300" icon="ic8_48_warning" text="On Hold" textfmt="plain">
                <note>Category: Waiting&#10;Requirement parked - not subject of current development; reason documented&#10;&#10;Responsible: Central Team / Vendor Team</note>
            </topic>

            <!-- CATEGORY: Terminal -->
            <topic id="13" parent="0" x="300" y="450" text="Terminal" textfmt="plain" palette="5">
                <layout mode="list" direction="auto" flow="auto"></layout>
            </topic>
            <topic id="7" parent="13" x="550" y="450" icon="ic8_48_finish_flag" text="Done" textfmt="plain">
                <note>Category: Terminal&#10;Requirement fully implemented and deployed to PROD; or rejected with justification&#10;&#10;Responsible: Central Team / Vendor Team</note>
            </topic>
        </topics>
        
        <!-- WORKFLOW RELATIONS -->
        <relations>
            <!-- Forward Flow -->
            <relation source="1" target="2"><children><text><note textfmt="plain">Accept &amp; Prioritize</note></text></children></relation>
            <relation source="2" target="3"><children><text><note textfmt="plain">Begin Analysis</note></text></children></relation>
            <relation source="3" target="4"><children><text><note textfmt="plain">Start Dev</note></text></children></relation>
            <relation source="4" target="7"><children><text><note textfmt="plain">Deploy to PROD</note></text></children></relation>
            
            <!-- Clarification Loop -->
            <relation source="3" target="5"><children><text><note textfmt="plain">Missing Info</note></text></children></relation>
            <relation source="5" target="3"><children><text><note textfmt="plain">Info Provided</note></text></children></relation>

            <!-- On Hold Loop -->
            <relation source="4" target="6"><children><text><note textfmt="plain">Park Issue</note></text></children></relation>
            <relation source="6" target="4"><children><text><note textfmt="plain">Resume Dev</note></text></children></relation>
        </relations>
    </mindmap>
</simplemind-mindmaps>
"""

os.makedirs("scratch/workflow_smmx/document", exist_ok=True)
with open("scratch/workflow_smmx/document/mindmap.xml", "w") as f:
    f.write(xml_content)

with zipfile.ZipFile("RequirementWorkflow.smmx", "w") as z:
    z.write("scratch/workflow_smmx/document/mindmap.xml", "document/mindmap.xml")

print("Created RequirementWorkflow.smmx!")
