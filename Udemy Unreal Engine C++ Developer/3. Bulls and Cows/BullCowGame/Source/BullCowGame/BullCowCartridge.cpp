#include "BullCowCartridge.h"
#include "HiddenWordList.h"

void UBullCowCartridge::BeginPlay() // When the game starts
{
    Super::BeginPlay();

    GetValidWords();

    SetupGame();
}

void UBullCowCartridge::GetValidWords()
{
    ValidWords.Empty();  // ensure starting from empty valid words list

    for (FString Word : Words)
    {
        if ((Word.Len() > 4) && (Word.Len() <= 8) && IsIsogram(Word))
        {
            ValidWords.Emplace(Word);
        }
    }
}

void UBullCowCartridge::OnInput(const FString& Input) // When the player hits enter
{    
    // win!
    if (Input == HiddenWord) 
    {
        PrintLine(TEXT("Congratulations, you win!"), *Input);
        EndGame();
        return;
    } 

    --Lives;
    PrintLine(TEXT("Incorrect, remaining lives: %i"), Lives);

    // game over
    if (Lives <= 0)
    {
        PrintLine(TEXT("Game Over."));
        PrintLine(TEXT("Hidden word was: %s"), *HiddenWord);
        EndGame();
        return;
    }

    // check # of characters
    if (HiddenWord.Len() != Input.Len())
    {
        PrintLine(TEXT("Hint: hidden word is %i characters."), HiddenWord.Len());
    }

    // check if isogram
    if (!IsIsogram(Input))
    {
        PrintLine(TEXT("Hint: no repeating characters."));
    }

    // check characters
    Bulls.Empty();
    Cows.Empty();
    for (int32 i = 0; i < Input.Len(); i++)
    {
        // check for bull
        if ((i < HiddenWord.Len()) && (Input[i] == HiddenWord[i]))
        {
            Bulls.Emplace(i, Input[i]);
        }

        // check for cow
        for (int32 k = 0; k < HiddenWord.Len(); k++)
        {
            if (Input[i] == HiddenWord[k])
            {
                Cows.AddUnique(Input[i]);
            }
        }
    }
    if (Bulls.Num() > 0)
    {
        FString BullsStr = "";
        for (auto& Bull : Bulls)
        {
            BullsStr += FString::FromInt(Bull.Key) + TEXT(":") + Bull.Value + TEXT(" ");
        }
        PrintLine(TEXT("Bulls: %s"), *BullsStr);
    }
    if (Cows.Num() > 0)
    {
        FString CowsStr = TEXT("");
        for (auto& Cow : Cows)
        {
            CowsStr.AppendChar(Cow);
            CowsStr += " ";
        }
        PrintLine(TEXT("Cows: %s"), *CowsStr);
    }
}

bool UBullCowCartridge::IsIsogram(const FString& Word) const
{
    for (int32 i = 0; i < Word.Len() - 1; i++)
    {
        for (int32 k = i + 1; k < Word.Len(); k++)
        {
            if (Word[i] == Word[k])
            {
                return false;
            }
        }
    }
    return true;
}

void UBullCowCartridge::SetupGame()
{
    // variable init
    HiddenWord = ValidWords[FMath::RandRange(0, ValidWords.Num() - 1)];
    Lives = HiddenWord.Len() * 2;

    // welcome the player
    ClearScreen();
    PrintLine(TEXT("Welcome to Bulls & Cows!"));
    PrintLine(TEXT("Guess the %i letter word."), HiddenWord.Len());
    PrintLine(TEXT("Type your guess then press enter."));
    PrintLine(TEXT("You have %i lives."), HiddenWord.Len());
}

void UBullCowCartridge::EndGame()
{
    PrintLine(TEXT("\nPress enter to play again."));
    //std::cin.get(); // TODO
    SetupGame();
}
