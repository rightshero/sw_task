let maxLevel = 1;

function generateCheckboxes(choice) {
  const currentLevel = parseInt(choice.getAttribute("data-level"));
  //   const id = choice.id;
  //   console.log(id);

  // If checkbox is unchecked, remove the lower level checkboxes
  if (!choice.checked) {
    removeLowerCheckboxes(currentLevel);
    return;
  }

  // Uncheck other checkboxes at the same level
  uncheckOtherCheckboxes(currentLevel, choice.id);

  const nextLevel = currentLevel + 1;
  const container = document.getElementById("checkbox-container");

  // Create a container for new checkboxes
  const newCheckboxesContainer = document.createElement("div");
  newCheckboxesContainer.id = nextLevel;
  newCheckboxesContainer.className = `level-${nextLevel}`;

  // Create new checkboxes for the next level
  const checkboxA = document.createElement("input");
  checkboxA.type = "checkbox";
  checkboxA.id = `level-${nextLevel}-A`;
  checkboxA.setAttribute("data-level", nextLevel);
  checkboxA.setAttribute("data-choice", "A");
  checkboxA.onclick = () => generateCheckboxes(checkboxA);

  const checkboxB = document.createElement("input");
  checkboxB.type = "checkbox";
  checkboxB.id = `level-${nextLevel}-B`;
  checkboxB.setAttribute("data-level", nextLevel);
  checkboxB.setAttribute("data-choice", "B");
  checkboxB.onclick = () => generateCheckboxes(checkboxB);

  // Append new checkboxes and labels to the new container
  newCheckboxesContainer.appendChild(checkboxA);
  newCheckboxesContainer.appendChild(
    document.createTextNode(` Choice A (Level ${nextLevel}) `)
  );
  //   newCheckboxesContainer.appendChild(document.createElement("br"));
  newCheckboxesContainer.appendChild(checkboxB);
  newCheckboxesContainer.appendChild(
    document.createTextNode(` Choice B (Level ${nextLevel})`)
  );
  newCheckboxesContainer.appendChild(document.createElement("br"));

  // Append the new container to the main container
  container.appendChild(newCheckboxesContainer);

  maxLevel = nextLevel;
}

function removeLowerCheckboxes(level) {
  const elementsToRemove = document.querySelectorAll('div[class^="level-"]');
  console.log(elementsToRemove);
  elementsToRemove.forEach((element) => {
    if (element.id > level) {
      element.remove();
    }
    console.log(`Checkbox ID: ${element.id}`);
  });
  // Update maxLevel if necessary
  if (level < maxLevel) {
    maxLevel = level;
  }
}

function uncheckOtherCheckboxes(level, checkedId) {
  const container = document.getElementById("checkbox-container");
  const checkboxesAtLevel = container.querySelectorAll(
    `.level-${level} input[type="checkbox"]`
  );

  checkboxesAtLevel.forEach((checkbox) => {
    console.log(checkbox.id);
    if (checkbox.id !== checkedId) {
      checkbox.checked = false; // Uncheck other checkboxes at the same level
      removeLowerCheckboxes(level);
    }
  });
}
