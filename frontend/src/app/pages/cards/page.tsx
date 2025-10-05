"use client";

import { useRouter } from 'next/navigation';
import { useEffect, useState } from "react";
import MyButton from "@/app/components/button";
import Card from "@/app/components/card";
import CardTranslated from '@/app/components/card_translated';
import styles from "../../page.module.css";
import "./page_style.css";


export default function Cards() {
  const router = useRouter();

  const [vocable, setVocable] = useState<string>("");
  const [tags, setTags] = useState<string[]>([]);
  const [translation, setTranslation] = useState<string>("");
  const [language, setLanguage] = useState<string>("fr");

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/cards')
      .then(response => {
        if (response.ok) {
          return response.json()
        }
      })
      .then(data => {
        setVocable(data.french);
        setTags(data.tag);
      })
      .catch(error => {
        setVocable("Test french");
      });
    }, []);

  function clickNewCard() {
    console.log("New Card clicked");
    fetch('http://127.0.0.1:8000/api/cards')
      .then(response => {
        if (response.ok) {
          return response.json()
        }
      })
      .then(data => {
        setVocable(data.french);
        setTags(data.tag);
      })
      .catch(error => {
        setVocable("Test french 2");
      });
  }

  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <div className="container">
          <h1>Cards Page</h1>
          <p>Lerne neue Vokables ganz easy!</p>
          {language === "fr" ? (
            <Card word={vocable} />
          ) : (
            <CardTranslated word={translation} />
          )}
          <div style={{ height: '20px' }}>
            <MyButton title="Next" onClickButton={() => clickNewCard()} />
          </div>
        </div>
          <MyButton title="Back to Home" onClickButton={() => router.push('/')} />
      </main>
    </div>
  );
}
