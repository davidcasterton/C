#include <iostream>
#include <ctime>

void PrintIntroduction(int Level)
{
	std::cout << "You are a secret angent breaking into a level " << Level << " secure server room." << std::endl;
	std::cout << "You need to enter the correct code to continue..." << std::endl;
}

bool PlayGame(int Level)
{
	PrintIntroduction(Level);

	const int CodeA = rand() % Level + 1;
	const int CodeB = rand() % Level + 1;
	const int CodeC = rand() % Level + 1;

	const int CodeSum = CodeA + CodeB + CodeC;
	const int CodeProduct = CodeA * CodeB * CodeC;

	std::cout << std::endl;
	std::cout << "+ There are 3 numbers in the code" << std::endl;
	std::cout << "+ The codes add-up to: " << CodeSum << std::endl;
	std::cout << "+ The codes multiply to give: " << CodeProduct << std::endl;

	int GuessA, GuessB, GuessC, GuessSum, GuessProduct;

	std::cin >> GuessA;
	std::cin >> GuessB;
	std::cin >> GuessC;

	std::cin.clear();  // clears any errors
	std::cin.ignore();  // discards the buffer

	GuessSum = GuessA + GuessB + GuessC;
	GuessProduct = GuessA * GuessB * GuessC;

	if (GuessSum == CodeSum && GuessProduct == CodeProduct) {
		return true;
	} else {
		return false;
	}
}

int main()
{
	srand(time(NULL));  // seeds random based on time of day

	int Level = 1;
	int MaxLevel = 5;

	while (Level <= MaxLevel)
	{
		bool bLevelComplete = PlayGame(Level);

		if (bLevelComplete)
		{
			++Level;
			std::cout << "Correct! Advancing to level " << Level << ".\n\n";
			std::cout << "LEVEL: " << Level << std::endl;
		}
		else
		{
			std::cout << "Incorrect. Try level " << Level << " again.\n" << std::endl;
		}
	}

	std::cout << "Congratulation, you have completed all levels." << std::endl;

	return 0;
}
