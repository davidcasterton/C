// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Console/Cartridge.h"
#include "BullCowCartridge.generated.h"

struct FBullsAndCows
{
	TMap<int32, TCHAR> Bulls;
	TArray<TCHAR> Cows;
};

UCLASS(ClassGroup=(Custom), meta=(BlueprintSpawnableComponent))
class BULLCOWGAME_API UBullCowCartridge : public UCartridge
{
	GENERATED_BODY()

	public:
	virtual void BeginPlay() override;
	void EndGame();
	FBullsAndCows GetBullsAndCows(const FString& Word);
	void GetValidWords();
	bool IsIsogram(const FString& Word) const;
	virtual void OnInput(const FString& Input) override;
	void SetupGame();

	private:
	FString HiddenWord;
	int32 Lives;
	TArray<FString> ValidWords;
};
