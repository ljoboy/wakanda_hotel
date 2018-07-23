-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le :  jeu. 05 juil. 2018 à 11:36
-- Version du serveur :  10.1.22-MariaDB
-- Version de PHP :  7.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `new_wakanda`
--

-- --------------------------------------------------------

--
-- Structure de la table `chambre`
--

CREATE TABLE `chambre` (
  `Id` int(20) NOT NULL,
  `Id_type` int(20) NOT NULL,
  `nom_chambre` varchar(50) NOT NULL,
  `details` varchar(255) DEFAULT NULL,
  `Disponibilite` varchar(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `chambre`
--

INSERT INTO `chambre` (`Id`, `Id_type`, `nom_chambre`, `details`, `Disponibilite`) VALUES
(2, 1, 'Focus', NULL, '1'),
(3, 1, 'Juste', NULL, '1'),
(4, 3, 'Justin', 'Un petit détails', '1');

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `Id` int(20) NOT NULL,
  `Nom_client` varchar(20) NOT NULL,
  `PostNom_client` varchar(20) NOT NULL,
  `Prenom_client` varchar(20) NOT NULL,
  `Email_client` varchar(20) NOT NULL,
  `Tel_client` varchar(20) NOT NULL,
  `Nationalite_client` varchar(20) NOT NULL,
  `Profession_client` varchar(20) NOT NULL,
  `Sexe_client` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`Id`, `Nom_client`, `PostNom_client`, `Prenom_client`, `Email_client`, `Tel_client`, `Nationalite_client`, `Profession_client`, `Sexe_client`) VALUES
(6, 'azertyui', 'zertyuiop', 'zertyuio', 'poiuytr@fghj.ddf', 'poiuytre', ';,nbvcxwq', 'edrfgyhuji', 'm'),
(7, ';mùljkjhg', 'zertyuiop', 'dcfvgbhjnkl', 'poiuytr@fghj.ddf', 'poiuytre', ';,nbvcxwq', 'edrfgyhuji', 'm'),
(8, 'swxdrctfgyhun', ';mùljkjhg', 'zertyuiop', 'poiuytr@fghj.ddf', 'dcfvgbhjnkl', 'poiuytr@fghj.ddf', 'poiuytre', 'qwsxd'),
(9, 'jkhjgh', 'kujytd', 'fghj', 'jklhl@gmail.com', ',jhgf', 'fcghvj', 'rtyuioui', 'm'),
(10, 'gringo', 'jaelly', 'gloire', 'gringo@rango.wk', 'Jireh', 'congolaise', 'azertyuio', 'm'),
(11, '', '', '', '', '', '', '', 'm'),
(12, 'sdrtcbuhijo', 'erxdcthgybukijokpl', 'drtcyubijokp', 'tdrgyukokpltcvybuijk', 'cghubjiokp;', 'cvubi;', 'cgvhbjkl,m;', 'f');

-- --------------------------------------------------------

--
-- Structure de la table `commande`
--

CREATE TABLE `commande` (
  `Id` int(50) NOT NULL,
  `prix_unitaire` double NOT NULL,
  `Nom_article` varchar(50) NOT NULL,
  `Nombre` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `facture`
--

CREATE TABLE `facture` (
  `Id` int(11) NOT NULL,
  `Prix_total` float NOT NULL,
  `Id_client` int(11) NOT NULL,
  `Montant_payee` double DEFAULT NULL,
  `Type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `menu`
--

CREATE TABLE `menu` (
  `Id` int(255) NOT NULL,
  `Nom_art` int(11) NOT NULL,
  `Prix_art` int(11) NOT NULL,
  `Stock` int(11) NOT NULL,
  `Details` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `payement`
--

CREATE TABLE `payement` (
  `Id` int(11) NOT NULL,
  `Id_commande` int(11) NOT NULL,
  `Id_facture` int(11) NOT NULL,
  `Type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `reservation`
--

CREATE TABLE `reservation` (
  `Id` int(50) NOT NULL,
  `Id_client` int(50) NOT NULL,
  `Id_chambre` int(50) NOT NULL,
  `Check_in` date NOT NULL,
  `Check_out` date NOT NULL,
  `Prix` double NOT NULL,
  `Details` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `type`
--

CREATE TABLE `type` (
  `Id` int(255) NOT NULL,
  `Prix_unitaire` double NOT NULL,
  `Nom_type` varchar(255) NOT NULL,
  `Detail_type` varchar(255) NOT NULL,
  `Nb_perso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `type`
--

INSERT INTO `type` (`Id`, `Prix_unitaire`, `Nom_type`, `Detail_type`, `Nb_perso`) VALUES
(1, 500, 'simple', '', 1),
(2, 800, 'double', '', 2),
(3, 1500, 'vip 1', '', 2),
(4, 5000, 'Blabla', 'Alors comme ca on veut un détails', 5);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `chambre`
--
ALTER TABLE `chambre`
  ADD PRIMARY KEY (`Id`);

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`Id`);

--
-- Index pour la table `commande`
--
ALTER TABLE `commande`
  ADD PRIMARY KEY (`Id`);

--
-- Index pour la table `facture`
--
ALTER TABLE `facture`
  ADD PRIMARY KEY (`Id`);

--
-- Index pour la table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`Id`);

--
-- Index pour la table `payement`
--
ALTER TABLE `payement`
  ADD PRIMARY KEY (`Id`);

--
-- Index pour la table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`Id`);

--
-- Index pour la table `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`Id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `chambre`
--
ALTER TABLE `chambre`
  MODIFY `Id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `client`
--
ALTER TABLE `client`
  MODIFY `Id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- AUTO_INCREMENT pour la table `commande`
--
ALTER TABLE `commande`
  MODIFY `Id` int(50) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `menu`
--
ALTER TABLE `menu`
  MODIFY `Id` int(255) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `payement`
--
ALTER TABLE `payement`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `reservation`
--
ALTER TABLE `reservation`
  MODIFY `Id` int(50) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `type`
--
ALTER TABLE `type`
  MODIFY `Id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
