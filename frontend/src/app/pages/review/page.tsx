"use client";
import { useEffect, useState } from "react";
import Card from "@/app/components/card";
import { MyButton } from "@/app/components/button";
import styles from "../../page.module.css";
import { useRouter } from 'next/navigation';

export default function Review() {
  const router = useRouter();
  const [vocable, setVocable] = useState<string>("");
  const [tags, setTags] = useState<string[]>([]);
  const [translation, setTranslation] = useState<string>("");

  useEffect(() => {
    fetch(process.env.NEXT_PUBLIC_BACKEND_URL + '/api/cards')
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
    fetch(process.env.NEXT_PUBLIC_BACKEND_URL + '/api/cards')
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
          <Card word={vocable} />
          <div style={{ height: '20px' }}>
            <MyButton title="Next" onClickButton={() => clickNewCard()} />
          </div>
        </div>
          <MyButton title="Back to Home" onClickButton={() => router.push('/')} />
      </main>
    </div>
  );
}
