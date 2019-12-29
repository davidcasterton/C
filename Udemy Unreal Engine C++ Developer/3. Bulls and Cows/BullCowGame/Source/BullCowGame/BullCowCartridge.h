// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Console/Cartridge.h"
#include "BullCowCartridge.generated.h"

UCLASS(ClassGroup=(Custom), meta=(BlueprintSpawnableComponent))
class BULLCOWGAME_API UBullCowCartridge : public UCartridge
{
	GENERATED_BODY()

	public:
	virtual void BeginPlay() override;
	void EndGame();
	void GetValidWords();
	bool IsIsogram(const FString& Word) const;
	virtual void OnInput(const FString& Input) override;
	void SetupGame();

	private:
	TMap<int32, TCHAR> Bulls;
    TArray<TCHAR> Cows;
	FString HiddenWord;
	int32 Lives;
	TArray<FString> ValidWords;
};
