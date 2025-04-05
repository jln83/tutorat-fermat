 // Écoute les changements dans le niveau
    niveauSelect.addEventListener("change", (event) => {
        const niveau = event.target.value;
        updateMatieres(niveau);
    });

    // Initialise les matières pour le niveau par défaut
    updateMatieres(niveauSelect.value);
});

document.addEventListener("DOMContentLoaded", () => {
    const timeInput = document.getElementById("time");

    // Fonction pour valider et ajuster l'heure sélectionnée
    const validateTime = () => {
        let [hours, minutes] = timeInput.value.split(":").map(Number);

        // Restreindre les heures entre 8 et 17
        if (hours < 8) hours = 8;
        if (hours > 17) hours = 17;

        // Ajuster les minutes pour être uniquement 00 ou 30
        if (minutes < 15) minutes = 0;
        else if (minutes < 45) minutes = 30;
        else {
            minutes = 0;
            hours = hours === 17 ? 8 : hours + 1; // Passer à l'heure suivante ou revenir à 8
        }

        // Formater et mettre à jour la valeur de l'entrée
        timeInput.value = `${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}`;
    };

    // Ajouter un écouteur d'événements pour valider l'heure à chaque modification
    timeInput.addEventListener("change", validateTime);

    // Définir une valeur par défaut correcte au chargement
    timeInput.value = "08:00";
});

document.addEventListener("DOMContentLoaded", () => {
    const dateInput = document.getElementById("date");

    // Liste des jours fériés pour l'année actuelle (et prochaine si nécessaire)
    const joursFeries = [
        "2025-01-01", // Jour de l'An
        "2025-04-21", // Lundi de Pâques
        "2025-05-01", // Fête du Travail
        "2025-05-08", // Victoire 1945
        "2025-05-29", // Ascension
        "2025-06-09", // Lundi de Pentecôte
        "2025-07-14", // Fête Nationale
        "2025-08-15", // Assomption
        "2025-11-01", // Toussaint
        "2025-11-11", // Armistice
        "2025-12-25", // Noël
    ];

    // Plages de vacances pour la zone C
    const vacancesZoneC = [
        { start: "2025-02-22", end: "2025-03-10" }, // Hiver
        { start: "2025-04-26", end: "2025-05-12" }, // Printemps
        { start: "2025-07-06", end: "2025-09-01" }, // Été
        { start: "2025-10-19", end: "2025-11-04" }, // Toussaint
        { start: "2025-12-21", end: "2026-01-06" }, // Noël
    ];

    // Fonction pour vérifier si une date est un week-end
    const isWeekend = (date) => {
        const day = date.getDay();
        return day === 0 || day === 6; // 0 = Dimanche, 6 = Samedi
    };

    // Fonction pour vérifier si une date est un jour férié
    const isJourFerie = (date) => {
        const dateString = date.toISOString().split("T")[0];
        return joursFeries.includes(dateString);
    };

    // Fonction pour vérifier si une date est pendant les vacances
    const isVacances = (date) => {
        const dateString = date.toISOString().split("T")[0];
        return vacancesZoneC.some(
            (vacances) =>
                dateString >= vacances.start && dateString <= vacances.end
        );
    };

    // Fonction principale pour désactiver les dates invalides
    const disableInvalidDates = () => {
        const today = new Date();
        dateInput.setAttribute("min", today.toISOString().split("T")[0]);

        dateInput.addEventListener("input", () => {
            const selectedDate = new Date(dateInput.value);

            if (
                isWeekend(selectedDate) ||
                isJourFerie(selectedDate) ||
                isVacances(selectedDate)
            ) {
                alert("La date choisie ne correspond pas à une date scolaire, merci d'en choisir une autre.");
                dateInput.value = ""; // Réinitialiser la sélection invalide
            }
        });
    };

    disableInvalidDates();
});