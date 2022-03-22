-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Czas generowania: 14 Mar 2022, 23:04
-- Wersja serwera: 5.7.37-0ubuntu0.18.04.1
-- Wersja PHP: 7.2.24-0ubuntu0.18.04.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `zse_tai3`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `cmsUsers`
--

CREATE TABLE `cmsUsers` (
  `id` int(4) NOT NULL,
  `active` int(1) NOT NULL DEFAULT '0',
  `logTry` int(1) NOT NULL DEFAULT '0',
  `lastLogin` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `email` varchar(40) NOT NULL,
  `user` varchar(40) NOT NULL,
  `name` varchar(25) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `surname` varchar(64) CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `passwd` varchar(120) NOT NULL,
  `token` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Zrzut danych tabeli `cmsUsers`
--

INSERT INTO `cmsUsers` (`id`, `active`, `logTry`, `lastLogin`, `email`, `user`, `name`, `surname`, `passwd`, `token`) VALUES
(1, 1, 0, '2020-02-19 23:00:00', 'jkreciwałek@zse.local', 'jkreciwałek', 'Jolanta', 'Kręciwałek', '12345Ty#', 'spc. ds. Zamówień publicznych '),
(2, 1, 0, '2020-02-19 23:00:00', 'fbrajanusz@zse.local', 'fbrajanusz', 'Fachmann', 'Brajanusz', '12345Ty#', 'spc. ds. Projektów Unijnych '),
(3, 1, 0, '2020-02-19 23:00:00', 'mnieda@zse.local', 'mnieda', 'Miranda', 'Nieda', '12345Ty#', 'kier. gospodarczy   '),
(4, 1, 0, '2020-02-19 23:00:00', 'mwcisnechlam@zse.local', 'mwcisnechlam', 'Marta', 'Wcisnechłam', '12345Ty#', 'spc. ds. sprzedaży  '),
(5, 1, 0, '2020-02-19 23:00:00', 'jdonos@zse.local', 'jdonos', 'Jacek', 'Donos', '12345Ty#', 'spc. ds. kontroli i bezpieczeństwa'),
(6, 1, 0, '2020-02-19 23:00:00', 'kstaraszkola@zse.local', 'kstaraszkola', 'Kazimierz', 'Staraszkoła', '12345Ty#', 'spc. ds. rozwoju  '),
(7, 1, 0, '2020-02-19 23:00:00', 'mkreda@zse.local', 'mkreda', 'Mariusz', 'Kreda', '12345Ty#', 'spc. ds. szkoleń  '),
(8, 1, 0, '2020-02-19 23:00:00', 'fnierusz@zse.local', 'fnierusz', 'Franciszek', 'Nierusz', '12345Ty#', 'spc. ds. technicznych  '),
(9, 1, 0, '2020-02-19 23:00:00', 'akasybrak@zse.local', 'akasybrak', 'Aldona', 'Kasybrak', '12345Ty#', 'spc. ds. finansowo-księgowych  '),
(10, 1, 0, '2020-02-19 23:00:00', 'bbezpamieci@zse.local', 'bbezpamieci', 'Barbara', 'Bezpamięci', '12345Ty#', 'spc. ds. planowania'),
(11, 1, 0, '2020-02-19 23:00:00', 'mwielepiej@zse.local', 'mwielepiej', 'Mirosław', 'Wielepiej', '12345Ty#', 'spc. ds. doradztwa biznesowego ');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `cmsUsers`
--
ALTER TABLE `cmsUsers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `cmsUsers`
--
ALTER TABLE `cmsUsers`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
