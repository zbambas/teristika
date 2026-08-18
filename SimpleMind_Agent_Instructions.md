# SimpleMind Mind Map (.smmx) Parsing Instructions for Agents

When tasked with reading or processing a SimpleMind mind map file (`.smmx`), follow these instructions to extract the data correctly.

## 1. File Extraction
A `.smmx` file is actually a ZIP archive. To read its contents, you first need to extract it.
- Use a terminal command like `unzip -o filename.smmx -d extract_dir` to unpack the file.
- Look for the main XML data file, which is typically located at `document/mindmap.xml` within the extracted directory.

## 2. XML Structure Overview
The XML file has a root element `<simplemind-mindmaps>` containing a `<mindmap>` element. The core data is divided into four main sections: `<meta>`, `<topics>`, `<relations>`, and `<node-groups>`.

### 2.1 Meta (`<meta>`)
This section contains global properties for the mind map.
- **`<style>`**: Defines the overall visual theme or style sheet used (e.g., `<style key="system.compact-gray-scale"></style>`). This controls default colors, topic shapes, and connection styles.

### 2.2 Topics (`<topics>`)
This section contains all the nodes (topics) in the mind map. Each node is represented by a `<topic>` element.

Key attributes and child elements of `<topic>`:
- **`id`**: The unique identifier for the topic (e.g., `id="0"`).
- **`parent`**: The ID of the parent topic. A value of `-1` indicates that the topic is a root or floating node.
- **`text`**: The main title or label of the node (e.g., `text="Issue: Requirement"`).
- **`date`**: (Optional) A deadline or event date assigned to the topic (e.g., `date="07-08-2026"`).
- **`checkbox`**: (Optional) Boolean indicating if the topic has a task tracker (e.g., `checkbox="true"`).
- **`checkbox-mode`**: (Optional) Specifies the type of tracker. Can be `progress` (paired with `progress="30"` for 30%) or `roll-up-progress` (calculates progress based on child topics).
- **`icon`**: (Optional) The name/ID of an icon assigned to the topic (e.g., `icon="ic8_48_create"`, `icon="ic8_48_high_priority"`). SimpleMind uses a set of built-in icons that typically start with `ic8_48_...`.
- **`<note>`** (Child Element): If the user added an extended description or note to the topic, it will be found inside a `<note>...</note>` tag within the `<topic>`.
- **`<layout>`** (Child Element): Specifies how the children of this node should be visually arranged. For example, `<layout mode="list" direction="auto" flow="auto"></layout>` specifies a list layout, while `mode="free"` specifies a free-form layout. If missing, the topic inherits the parent or default layout.
- **`<embedded-image>`** (Child Element): Represents an inline image inside the topic. Contains a `name` attribute which corresponds to a file in the `images/` directory of the unzipped archive (e.g., `images/{name}.png`). It may also have a `link` attribute pointing to an external file or URL.
- **`<image>`** (Child Element, inside `<children>` or `<images>`): Represents a floating image attached to the topic. Like `<embedded-image>`, it contains a `name` attribute corresponding to a `.png` file in the `images/` directory.

### 2.3 Relations (`<relations>`)
This section defines the cross-links or explicit connections (arrows) between topics that are not just standard hierarchical parent-child relationships.

Key attributes and child elements of `<relation>`:
- **`source`**: The `id` of the topic where the relation starts.
- **`target`**: The `id` of the topic where the relation ends.
- **Label / Text**: If the relation line has a label (e.g., "Creates"), it is nested inside the relation as follows:
  ```xml
  <relation source="4" target="0">
      <children>
          <text>
              <note textfmt="plain">Creates</note>
          </text>
      </children>
  </relation>
  ```

### 2.4 Node Groups (`<node-groups>`)
This section defines visual boundaries (group borders) drawn around sets of topics.
- Contains `<node-group>` elements, each with a `<style>` (defining colors and padding).
- Contains a `<topics>` child element listing the `id` of each topic included in the group (e.g., `<topic id="5"></topic>`).

## 3. Data Extraction Strategy
1. **Unzip** the `.smmx` file to a temporary location.
2. **Parse** `document/mindmap.xml`.
3. **Extract Meta**: Read the `<meta>` section to identify the overall mind map properties like the `<style>` key to understand the default aesthetic rules.
4. **Map Nodes**: Iterate through `<topics>` to build a dictionary mapping `id` to its `text`, `parent`, `icon` (if present), `<layout>` mode (if present), task/date attributes, and any `<note>` content.
5. **Build Hierarchy**: Use the `parent` attributes to reconstruct the tree structure.
6. **Extract Relations**: Iterate through `<relations>` to identify cross-links between topics, extracting the `source`, `target`, and the relation's label from `<children><text><note>`.
7. **Extract Groups**: Iterate through `<node-groups>` to identify visual clusters and the topic IDs that belong to them.
8. **Extract Images**: When a topic contains an `<embedded-image>` or `<image>`, use its `name` attribute to locate the actual image file in the extracted `images/` directory (append `.png`).
